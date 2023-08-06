#! /usr/bin/python
# -*- coding: utf-8 -*-

import tensorlayerx as tlx
from tensorlayerx import logging
from tensorlayerx.nn.core import Module

__all__ = ['OneHot', 'Word2vecEmbedding', 'Embedding', 'AverageEmbedding']


class OneHot(Module):
    """
    The :class:`OneHot` class is the starting layer of a neural network, see ``tf.one_hot``.
    Useful link: `https://www.tensorflow.org/api_docs/python/tf/one_hot`.

    Parameters
    ----------
    depth : None or int
        If the input indices is rank N, the output will have rank N+1. The new axis is created at dimension `axis` (default: the new axis is appended at the end).
    on_value : None or number
        The value to represnt `ON`. If None, it will default to the value 1.
    off_value : None or number
        The value to represnt `OFF`. If None, it will default to the value 0.
    axis : None or int
        The axis.
    dtype : None or TensorFlow dtype
        The data type, None means tlx.float32.
    name : str
        A unique layer name.

    Examples
    ---------
    >>> net = tlx.nn.Input([32], dtype=tlx.int32)
    >>> onehot = tlx.nn.OneHot(depth=8)
    >>> print(onehot)
    OneHot(depth=8, name='onehot')
    >>> tensor = tlx.nn.OneHot(depth=8)(net)
    >>> print(tensor)
    Tensor([...], shape=(32, 8), dtype=float32)

    """

    def __init__(self, depth=None, on_value=1.0, off_value=0.0, axis=-1, dtype=tlx.float32, name=None):
        super(OneHot, self).__init__(name)
        self.depth = depth
        self.on_value = on_value
        self.off_value = off_value
        self.axis = axis
        self.dtype = dtype
        logging.info("OneHotInput  %s" % (self.name))

        self.build()
        self._built = True

        if self.depth is None:
            raise RuntimeError(self.__class__.__name__ + ": depth == None the number of output units is undefined")

    def __repr__(self):
        s = ('{classname}(depth={depth}')
        if self.on_value is not None:
            s += ', on_value={on_value}'
        if self.off_value is not None:
            s += ', off_value={off_value}'
        if self.axis is not None:
            s += ', axis={axis}'
        if self.name is not None:
            s += ', name=\'{name}\''
        s += ')'
        return s.format(classname=self.__class__.__name__, **self.__dict__)

    def build(self, inputs_shape=None):
        self.onehot = tlx.ops.OneHot(
            depth=self.depth, on_value=self.on_value, off_value=self.off_value, axis=self.axis, dtype=self.dtype
        )

    def forward(self, inputs):
        """
        Parameters
        ----------
        inputs : input tensor
            The inputs are indices. The locations represented by indices in indices take value on_value, while all other locations take value off_value.
        """
        outputs = self.onehot(inputs)

        if not self._nodes_fixed and self._build_graph:
            self._add_node(inputs, outputs)
            self._nodes_fixed = True
        return outputs


class Word2vecEmbedding(Module):
    """
    The :class:`Word2vecEmbedding` class is a fully connected layer.
    For Word Embedding, words are input as integer index.
    The output is the embedded word vector.

    The layer integrates NCE loss by default (activate_nce_loss=True).
    If the NCE loss is activated, in a dynamic model,
    the computation of nce loss can be turned off in customised forward feeding
    by setting use_nce_loss=False when the layer is called.
    The NCE loss can be deactivated by setting activate_nce_loss=False.

    Parameters
    ----------
    num_embeddings : int
        size of the dictionary of embeddings.
    embedding_dim  : int
         the size of each embedding vector.
    num_sampled : int
        The number of negative examples for NCE loss
    activate_nce_loss : boolean
        Whether activate nce loss or not. By default, True
        If True, the layer will return both outputs of embedding and nce_cost in forward feeding.
        If False, the layer will only return outputs of embedding.
        In a dynamic model, the computation of nce loss can be turned off in forward feeding
        by setting use_nce_loss=False when the layer is called.
        In a static model, once the model is constructed, the computation of nce loss
        cannot be changed (always computed or not computed).
    nce_loss_args : dictionary
        The arguments for tf.ops.nce_loss()
    E_init : initializer or str
        The initializer for initializing the embedding matrix
    nce_W_init : initializer or str
        The initializer for initializing the nce decoder weight matrix
    nce_b_init : initializer or str
        The initializer for initializing of the nce decoder bias vector
    name : str
        A unique layer name

    Attributes
    ----------
    outputs : Tensor
        The embedding layer outputs.
    normalized_embeddings : Tensor
        Normalized embedding matrix.
    nce_weights : Tensor
        The NCE weights only when activate_nce_loss is True.
    nce_biases: Tensor
        The NCE biases only when activate_nce_loss is True.

    Examples
    --------
    Word2Vec With TensorLayer (Example in `examples/text_word_embedding/tutorial_word2vec_basic.py`)

    >>> import tensorlayerx as tlx
    >>> batch_size = 8
    >>> embedding_dim = 50
    >>> inputs = tlx.nn.Input([batch_size], dtype=tlx.int32)
    >>> labels = tlx.nn.Input([batch_size, 1], dtype=tlx.int32)
    >>> emb_net = tlx.nn.Word2vecEmbedding(
    >>>     num_embeddings=10000,
    >>>     embedding_dim=embedding_dim,
    >>>     num_sampled=100,
    >>>     activate_nce_loss=True, # the nce loss is activated
    >>>     nce_loss_args={},
    >>>     E_init=tlx.initializers.random_uniform(minval=-1.0, maxval=1.0),
    >>>     nce_W_init=tlx.initializers.truncated_normal(stddev=float(1.0 / np.sqrt(embedding_dim))),
    >>>     nce_b_init=tlx.initializers.constant(value=0.0),
    >>>     name='word2vec_layer',
    >>> )
    >>> print(emb_net)
    Word2vecEmbedding(num_embeddings=10000, embedding_dim=50, num_sampled=100, activate_nce_loss=True, nce_loss_args={})
    >>> embed_tensor = emb_net(inputs, use_nce_loss=False) # the nce loss is turned off and no need to provide labels
    >>> embed_tensor = emb_net([inputs, labels], use_nce_loss=False) # the nce loss is turned off and the labels will be ignored
    >>> embed_tensor, embed_nce_loss = emb_net([inputs, labels]) # the nce loss is calculated
    >>> outputs = tlx.nn.Linear(out_features=10, name="linear")(embed_tensor)
    >>> model = tlx.model.Model(inputs=[inputs, labels], outputs=[outputs, embed_nce_loss], name="word2vec_model") # a static model
    >>> out = model([data_x, data_y], is_train=True) # where data_x is inputs and data_y is labels

    References
    ----------
    `https://www.tensorflow.org/tutorials/representation/word2vec`

    """

    def __init__(
        self,
        num_embeddings,
        embedding_dim,
        num_sampled=64,
        activate_nce_loss=True,
        nce_loss_args=None,
        E_init='random_uniform',
        nce_W_init='truncated_normal',
        nce_b_init='constant',
        name=None,  #'word2vec',
    ):

        super(Word2vecEmbedding, self).__init__(name)
        self.num_embeddings = num_embeddings
        self.embedding_dim = embedding_dim
        self.num_sampled = num_sampled
        self.E_init = self.str_to_init(E_init)
        self.activate_nce_loss = activate_nce_loss

        if self.activate_nce_loss:
            self.nce_loss_args = nce_loss_args
            self.nce_W_init = self.str_to_init(nce_W_init)
            self.nce_b_init = self.str_to_init(nce_b_init)

        if not self._built:
            self.build(tuple())
            self._built = True

        logging.info("Word2vecEmbedding %s: (%d, %d)" % (self.name, self.num_embeddings, self.embedding_dim))

    def __repr__(self):
        s = ('{classname}(')
        s += 'num_embeddings={num_embeddings}'
        s += ', embedding_dim={embedding_dim}'
        s += ', num_sampled={num_sampled}'
        s += ', activate_nce_loss={activate_nce_loss}'
        if self.activate_nce_loss:
            s += ', nce_loss_args={nce_loss_args}'
        s += ')'
        return s.format(classname=self.__class__.__name__, **self.__dict__)

    def build(self, inputs_shape):
        """
        Parameters
        ----------
        inputs_shape : tuple
            the shape of inputs tensor
        """
        # Look up embeddings for inputs.
        # Note: a row of 'embeddings' is the vector representation of a word.
        # for the sake of speed, it is better to slice the embedding matrix
        # instead of transferring a word id to one-hot-format vector and then
        # multiply by the embedding matrix.
        # embed is the outputs of the hidden layer (embedding layer), it is a
        # row vector with 'embedding_dim' values.

        self.embeddings = self._get_weights(
            "embeddings",
            shape=(self.num_embeddings, self.embedding_dim),
            init=self.E_init,
        )

        self.normalized_embeddings = tlx.L2Normalize(axis=1)(self.embeddings)

        if self.activate_nce_loss:
            # Construct the variables for the NCE loss (i.e. negative sampling)
            self.nce_weights = self._get_weights(
                "nce_weights",
                shape=(self.num_embeddings, self.embedding_dim),
                init=self.nce_W_init,
            )

            self.nce_biases = self._get_weights(
                "nce_biases",
                shape=(self.num_embeddings, ),
                init=self.nce_b_init,
            )

        self.embedding_lookup = tlx.EmbeddingLookup()

        if self.activate_nce_loss:
            self.nce_loss = tlx.NCELoss(**self.nce_loss_args)

    def forward(self, inputs, use_nce_loss=None):
        """
        Parameters
        ----------
        inputs : tensor or list
            If the nce loss is activated and is used, the argument should be a list of two tensors [inputs, labels].
            Otherwise, the argument should be a single tensor which is inputs.
        use_nce_loss: boolean
            Whether use NCE loss in this run.
            If the nce loss is used, the activate_nce_loss should be True when the layer is initialized.
            By default, same as activate_nce_loss.

        Outputs:
        ----------
        outputs: tensor
        nce_cost: tensor
            The nce_cost is returned only if the nce_loss is used.
        """

        if isinstance(inputs, list):
            outputs = self.embedding_lookup(params=self.embeddings, ids=inputs[0])
        else:
            outputs = self.embedding_lookup(params=self.embeddings, ids=inputs)

        if use_nce_loss is True and not self.activate_nce_loss:
            raise AttributeError(
                "The nce loss is not activated when the %s is initialized. Please set activate_nce_loss=True." %
                self.__class__.__name__
            )

        if self.activate_nce_loss and (use_nce_loss is True or use_nce_loss is None):
            if not isinstance(inputs, list):
                raise ValueError("If nce loss is used, the labels of inputs must be provided.")

            nce_cost = tlx.ops.reduce_mean(
                input_tensor=self.nce_loss(
                    weights=self.nce_weights, biases=self.nce_biases, inputs=outputs, labels=inputs[1],
                    num_sampled=self.num_sampled, num_classes=self.num_embeddings
                )
            )

            if not self._nodes_fixed and self._build_graph:
                self._add_node(inputs, [outputs, nce_cost])
                self._nodes_fixed = True
            return outputs, nce_cost

        if not self._nodes_fixed and self._build_graph:
            self._add_node(inputs, outputs)
            self._nodes_fixed = True
        return outputs


class Embedding(Module):
    """
    A simple lookup table that stores embeddings of a fixed dictionary and size.

    This module is often used to store word embeddings and retrieve them using indices.
    The input to the module is a list of indices, and the output is the corresponding word embeddings.

    Parameters
    ----------
    num_embeddings : int
        size of the dictionary of embeddings.
    embedding_dim  : int
         the size of each embedding vector.
    E_init : initializer or str
        The initializer for the embedding matrix.
    E_init_args : dictionary
        The arguments for embedding matrix initializer.
    name : str
        A unique layer name.

    Attributes
    ----------
    outputs : tensor
        The embedding layer output is a 3D tensor in the shape: (batch_size, num_steps(num_words), embedding_dim).

    Examples
    --------
    >>> import tensorlayerx as tlx
    >>> input = tlx.nn.Input([8, 100], dtype=tlx.int32)
    >>> embed = tlx.nn.Embedding(num_embeddings=1000, embedding_dim=50, name='embed')
    >>> print(embed)
    Embedding(num_embeddings=1000, embedding_dim=50)
    >>> tensor = embed(input)
    >>> print(tensor)
    Tensor([...], shape=(8, 100, 50), dtype=float32)

    """

    def __init__(
        self,
        num_embeddings,
        embedding_dim,
        E_init='random_uniform',
        name=None,  #'embedding',
    ):
        super(Embedding, self).__init__(name)
        self.num_embeddings = num_embeddings
        self.embedding_dim = embedding_dim
        self.E_init = self.str_to_init(E_init)

        if not self._built:
            self.build(tuple())
            self._built = True

        logging.info("Embedding %s: (%d, %d)" % (self.name, self.num_embeddings, self.embedding_dim))

    def __repr__(self):
        s = ('{classname}(')
        s += 'num_embeddings={num_embeddings}'
        s += ', embedding_dim={embedding_dim}'
        s += ')'
        return s.format(classname=self.__class__.__name__, **self.__dict__)

    def build(self, inputs_shape):
        """
        Parameters
        ----------
        inputs_shape : tuple
            the shape of inputs tensor
        """

        self.embeddings = self._get_weights(
            "embeddings",
            shape=(self.num_embeddings, self.embedding_dim),
            init=self.E_init,
        )
        self.embedding_lookup = tlx.EmbeddingLookup()

    def forward(self, inputs):
        """
        Parameters
        ----------
        inputs : Tensor
            The input of a network.
        """
        outputs = self.embedding_lookup(params=self.embeddings, ids=inputs)

        if not self._nodes_fixed and self._build_graph:
            self._add_node(inputs, outputs)
            self._nodes_fixed = True
        return outputs


class AverageEmbedding(Module):
    """The :class:`AverageEmbedding` averages over embeddings of inputs.
    This is often used as the input layer for model like DAN[1] and FastText[2].

    Parameters
    ----------
    num_embeddings : int
        size of the dictionary of embeddings.
    embedding_dim  : int
         the size of each embedding vector.
    pad_value : int
        The scalar padding value used in inputs, 0 as default.
    E_init : initializer or str
        The initializer of the embedding matrix.
    name : str
        A unique layer name.

    Attributes
    ----------
    outputs : tensor
        The embedding layer output is a 2D tensor in the shape: (batch_size, embedding_dim).

    References
    ----------
    - [1] Iyyer, M., Manjunatha, V., Boyd-Graber, J., & Daum’e III, H. (2015). Deep Unordered Composition Rivals Syntactic Methods for Text Classification. In Association for Computational Linguistics.
    - [2] Joulin, A., Grave, E., Bojanowski, P., & Mikolov, T. (2016). `Bag of Tricks for Efficient Text Classification. <http://arxiv.org/abs/1607.01759>`__

    Examples
    ---------
    >>> import tensorlayerx as tlx
    >>> batch_size = 8
    >>> length = 5
    >>> input = tlx.nn.Input([batch_size, length], dtype=tlx.int32)
    >>> avgembed = tlx.nn.AverageEmbedding(num_embeddings=1000, embedding_dim=50, name='avg')
    >>> print(avgembed)
    AverageEmbedding(num_embeddings=1000, embedding_dim=50, pad_value=0)
    >>> tensor = avgembed(input)
    >>> print(tensor)
    Tensor([...], shape=(8, 50), dtype=float32)

    """

    def __init__(
        self,
        num_embeddings,
        embedding_dim,
        pad_value=0,
        E_init='random_uniform',
        name=None,  # 'average_embedding',
    ):

        super(AverageEmbedding, self).__init__(name)
        self.num_embeddings = num_embeddings
        self.embedding_dim = embedding_dim
        self.pad_value = pad_value
        self.E_init = self.str_to_init(E_init)

        if not self._built:
            self.build(tuple())
            self._built = True

        logging.info("AverageEmbedding %s: (%d, %d)" % (self.name, self.num_embeddings, self.embedding_dim))

    def __repr__(self):
        s = ('{classname}(')
        s += 'num_embeddings={num_embeddings}'
        s += ', embedding_dim={embedding_dim}'
        s += ', pad_value={pad_value}'
        s += ')'
        return s.format(classname=self.__class__.__name__, **self.__dict__)

    def build(self, inputs_shape):
        """
        Parameters
        ----------
        inputs_shape : tuple
            the shape of inputs tensor.
        """
        # if len(inputs_shape) != 2:
        #     raise ValueError('inputs must be of size (batch_size, sentence_length)')

        self.embeddings = self._get_weights(
            "embeddings",
            shape=(self.num_embeddings, self.embedding_dim),
            init=self.E_init,
        )
        self.embedding_lookup = tlx.EmbeddingLookup()
        self.not_equal = tlx.NotEqual()
        self.cast = tlx.Cast(tlx.float32)
        self.expand_dims = tlx.ExpandDims(axis=-1)
        self.reduce_sum = tlx.ReduceSum(axis=1)
        self.count_nonzero = tlx.CountNonzero(keepdims=True, dtype=tlx.float32)

    def forward(self, inputs):
        """
        Parameters
        ----------
        inputs : tensor
            The network input.
            For word inputs, please use integer index format, 2D tensor: (batch_size, sentence_length).
        """
        word_embeddings = self.embedding_lookup(params=self.embeddings, ids=inputs)

        # Zero out embeddings of pad value
        masks = self.not_equal(inputs, self.pad_value)
        word_embeddings *= self.cast(self.expand_dims(masks))
        sum_word_embeddings = self.reduce_sum(input=word_embeddings)

        # Count number of non-padding words in each sentence
        sentence_lengths = self.count_nonzero(masks, axis=1)
        sentence_embeddings = tlx.ops.divide(
            sum_word_embeddings,
            sentence_lengths + 1e-8,  # Add epsilon to avoid dividing by 0
        )

        outputs = sentence_embeddings

        if not self._nodes_fixed and self._build_graph:
            self._add_node(inputs, outputs)
            self._nodes_fixed = True
        return outputs
