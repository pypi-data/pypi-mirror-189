# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['efnlp']

package_data = \
{'': ['*']}

install_requires = \
['protobuf==3.20']

setup_kwargs = {
    'name': 'efnlp',
    'version': '0.1.1',
    'description': 'Empirical Frequency Natural Language Processing',
    'long_description': '# efnlp\n\nThis is the _jankiest possible_ take at computing n-gram or conditional empirical frequency ((C)EF) distributions for successor tokens given a fixed-width prefix. Yes that\'s just a Markov model. In a way this is _purposefully_ naive, and interested in how far such a naive technique goes. \n\nThere\'s `python` and `c++` code (in [`efnlp`](/efnlp) and [`cpp`](/cpp) respectively) for analyzing text and creating sampling datastructures. There\'s also `go` code (in [`go`](/go)) for a gRPC server to read sampling datastructures and serve batch or streaming generated text. \n\n## Motivation (even though we just playin)\n\nThe basic idea is to explore computing these values and using them in generative sampling tasks. We "hypothesize" that the asymptotic (in data and model class universality) result of computational [(L)LMs](https://en.wikipedia.org/wiki/Language_model) is a high-fidelity representation of the (C)EF in the training data. This is a bit tautologous, for a consistent statistical model estimated on sufficient data. See `paper/*.pdf` for more; however I have had repeated personal experiences with really cool complicated models basically reducing to the information in counts and averages, much like (C)EFs. \n\nOf course, a (C)EF "model" should have serious generalizability challenges when confronted with valid sequences not appearing in the training data. Particularly if we wish to generate text (via token sequences), we may generate sequences purely by chance that have no (or limited) precedent and thus have limited predictive capacity. (A Markov model can always reduce to token occurrence frequencies, though randomly choosing tokens is far from language modeling.) This is a primary goal of statistical models: to find (or use) structure to "fill in the gaps" of a particular corpus of training data. However, as a training corpus grows to encompass more and more of the possibilities of discourse, the likelihood we have not "seen" a valid sequence should also decrease, and a model should also be getting progressively more aligned with the (C)EFs. \n\nAlso we would expect the required storage for a purely (C)EF "model" to grow quite large. This is, in principal, another primary goal of statistical models: to "compress" statistical information without diminishing validation/generalization performance. Yet, the SOTA statistical models are themselves quite extraordinarily large; samples are not reasonable computable on a single machine, involving many billions of parameters and linear algebra involved enough to require specialized hardware. \n\nObviously if simple (C)EF models were of comparable quality to modern LLMs they would be making all the noise instead. This isn\'t about a better approach, just a personal investigation. \n\n## Example \n\nYou can run the `python` code from the CLI as\n```shell\n$ python -m efnlp -c data/tinywillspeare.txt -m -s -b 10 -g 100000 -o sample-results.txt\n[2023-01-28T21:37:56.223686 | 0.000020s] Reading text corpus\n[2023-01-28T21:37:56.225040 | 0.001374s] Forming (character) language\n[2023-01-28T21:37:56.273636 | 0.049969s] Encoding corpus in the language constructed\n[2023-01-28T21:37:56.345648 | 0.122002s] Corpus is 1,115,393 tokens long\n[2023-01-28T21:37:56.345711 | 0.122036s] Parsing prefix/successor tokens\n[2023-01-28T21:38:24.269634 | 28.045963s] Parsed prefixes and successors in corpus in 27923.90ms\n[2023-01-28T21:38:27.680794 | 31.457128s] Found 858,920 prefixes (77.0% of possible)\n[2023-01-28T21:38:34.836321 | 38.612656s] Found 937,254 patterns (84.0% of possible)\n[2023-01-28T21:38:37.554198 | 41.330531s] Memory (roughly) required: 31.9 MB (about 4,177,347 dbl, 8,354,695 fl)\n[2023-01-28T21:38:37.554237 | 41.330562s] Sampling and decoding 100000 tokens\n[2023-01-28T21:38:38.493836 | 42.270165s] Generation frequency: 9.4 us/tok\n[2023-01-28T21:38:38.493869 | 42.270194s] Writing sampled results to sample-results.txt\n```\n(for which you can see generated text in [`results`](/sample-results.txt)). The compiled `c++` is similar, \n```shell\ncpp$ ./efnlp++ -c data/tinywillspeare.txt -m -s -b 10 -g 100000 -o sample-results.txt\n```\nor the `go`\n```shell\ngo$ go run *.go -parse \\\n\t-input ../data/tinywillspeare.txt \\\n\t-language ../cpp/language.proto.bin \\\n\t-block 10 \\\n\t-generate 10000 \\\n\t-print=false\n```\n(note the use of a `language` datastructure in `proto` format). \n\nOur "model" here (in `python`) is, more or less, 8M `double`s worth of "parameters" and "trains" (estimates) in a single process on an (old) macbook in under a minute (for 10-token sequence statistics). Sampling is basically constant time, relying on hashmaps; the example above takes about 0.1ms per character sampled (with zero code optimizations). The (C)EF "model" are a significant inflation of the data size: 1.1MB of data turns into 62.4MB of statistics. But honestly the results aren\'t that bad. It\'s junk of course, but on the surface comparable to generative text from a 10M parameter transformer style model applied to the same dataset that trained for 15 minutes on a GPU ([tweet here](https://twitter.com/karpathy/status/1615400286293753856?cxt=HHwWgIDUqY2Ah-ssAAAA), [code here](https://github.com/karpathy/nanoGPT)). \n\nThe full CLI arg list can be reviewed from\n```shell\n$ python -m efnlp -h\n```\n\nMore comprehensive results are detailed in the following tables (see `paper/*.pdf` for more discussion): \n\n| B | \\# prefixes | unique pref. | \\# pattern | unique patt. | avg succ./pref. | memory |\n| --- | --- | --- | --- | --- | --- | --- |\n|  1 | 65 | 0.0\\% | 1,403 | 0.1\\% | 21.6 | 3kB |\n|  2 | 1,403 | 0.1\\% | 11,556 | 1.0\\% | 8.2 | 36kB |\n|  3 | 11,556 | 1.0\\% | 50,712 | 4.5\\% | 4.4 | 221kB |\n|  4 | 50,712 | 4.5\\% | 141,021 | 12.6\\% | 2.8 | 876kB |\n|  5 | 141,021 | 12.6\\% | 283,313 | 25.4\\% | 2.0 | 2.5MB |\n|  7 | 447,352 | 40.1\\% | 609,659 | 54.7\\% | 1.4 | 10.1MB |\n| 10 | 858,920 | 77.0\\% | 937,254 | 84.0\\% | 1.1 | 31.9MB |\n| 12 | 991,391 | 88.9\\% | 1,027,857 | 92.2\\% | 1.0 | 50.4MB |\n| 15 | 1,069,423 | 95.9\\% | 1,081,060 | 96.9\\% | 1.0 | 80.6MB |\n| 20 | 1,103,358 | 98.9\\% | 1,106,345 | 99.2\\% | 1.0 | 133MB |\n\nWhat follows are comparative parsing/generation speeds (for sampling 1M tokens):\n\n|  B  | py parse | py t/&tau; | go parse | go t/&tau; | c++ parse | c++ t/&tau; |\n| --- | ------ | --------- | ----- | -------- | ----- | -------- |\n|  1  | 1.0s   |  1.4&mu;s |  49ms | 0.1&mu;s | 131ms | 0.1&mu;s |\n|  2  | 2.0s   |  1.7&mu;s | 109ms | 0.1&mu;s | 248ms | 0.2&mu;s |\n|  3  | 3.3s   |  2.1&mu;s | 222ms | 0.2&mu;s | 419ms | 0.3&mu;s |\n|  4  | 4.3s   |  2.6&mu;s | 361ms | 0.3&mu;s | 612ms | 0.4&mu;s |\n|  5  | 6.4s   |  3.2&mu;s | 585ms | 0.5&mu;s |  1.1s | 0.5&mu;s |\n|  7  | 12.0s  |  4.9&mu;s |  1.2s | 0.7&mu;s |  2.0s | 0.7&mu;s |\n| 10  | 28.0s  |  7.0&mu;s |  2.6s | 0.9&mu;s |  1.9s | 0.8&mu;s |\n| 12  | 37.3s  |  8.3&mu;s |  4.1s | 1.1&mu;s |  2.5s | 1.0&mu;s |\n| 15  | 54.3s  |  9.7&mu;s |  5.2s | 1.2&mu;s |  3.2s | 1.0&mu;s |\n| 20  | 129.0s | 12.7&mu;s |  8.4s | 1.6&mu;s |  4.4s | 1.3&mu;s |\n\n\nNote (until we get better formatting) that the repeated "parse" (parse time) and "t/&tau;" (time per token) columns are for `python`, `go`, and `c++` respectively. With each we can generate text at O(&mu;s)/token. However compiled codes (`go` and `c++`) are faster (roughly by an order of magnitude) and seem to scale a bit better with longer sequences. With compiled code we can parse out the (C)EFs in shakespeare in seconds; while `python` is still "reasonable" it takes a couple minutes to parse 20-token sequences. \n\n## Usage\n\n### python\n\nSee [`efnlp/__main__.py`](/efnlp/__main__.py) for an example of running the no-doubt-dumb implementations in [`efnlp/__init__.py`](/efnlp/__init__.py). \n\n### c++\n\nSee [`cpp/*`](/cpp), with stuff that should be ready for `cmake` to run through a build. Embarassingly, pretty much everything is just in [`main.cpp`](/cpp/main.cpp). \n\n### go\n\nSee [`go/*`](/go), with stuff that should be ready to build. There\'s a very brief [`README.md`](/go/README.md) \n\n',
    'author': 'W. Ross Morrow',
    'author_email': 'morrowwr@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
