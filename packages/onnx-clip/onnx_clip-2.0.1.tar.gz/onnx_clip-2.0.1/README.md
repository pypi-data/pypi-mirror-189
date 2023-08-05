# onnx_clip

An [ONNX](https://onnx.ai/)-based implementation of [CLIP](https://github.com/openai/CLIP) that doesn't
depend on `torch` or `torchvision`.

This works by
- running the text and vision encoders (the ViT-B/32 variant) in [ONNX Runtime](https://onnxruntime.ai/)
- using a pure NumPy version of the tokenizer
- using a pure NumPy+PIL version of the [preprocess function](https://github.com/openai/CLIP/blob/3702849800aa56e2223035bccd1c6ef91c704ca8/clip/clip.py#L79).
  The PIL dependency could also be removed with minimal code changes - see `preprocessor.py`.

## git lfs
This repository uses Git LFS for the `.onnx` files of the image and text models.
Make sure to do `git lfs install` before cloning.

In case you use the `onnx_clip` project not as a repo, but as a package,
the models will be downloaded from the public S3 bucket:
[image model](https://lakera-clip.s3.eu-west-1.amazonaws.com/clip_image_model_vitb32.onnx),
[text model](https://lakera-clip.s3.eu-west-1.amazonaws.com/clip_text_model_vitb32.onnx).

## Installation
To install, run the following in the root of the repository:
```bash
pip install .
```

## Usage

All you need to do is call the `OnnxClip` model class. An example:

```python
from onnx_clip import OnnxClip, softmax, get_similarity_scores
from PIL import Image

images = [Image.open("onnx_clip/data/franz-kafka.jpg").convert("RGB")]
texts = ["a photo of a man", "a photo of a woman"]

onnx_model = OnnxClip()

# Unlike the original CLIP, there is no need to run tokenization/preprocessing
# separately - simply run get_image_embeddings directly on PIL images/NumPy
# arrays, and run get_text_embeddings directly on strings.
image_embeddings = onnx_model.get_image_embeddings(images)
text_embeddings = onnx_model.get_text_embeddings(texts)

# To use the embeddings for zero-shot classification, you can use these two
# functions. Here we run on a single image, but any number is supported.
logits = get_similarity_scores(image_embeddings, text_embeddings)
probabilities = softmax(logits)

print("Logits:", logits)

for text, p in zip(texts, probabilities[0]):
    print(f"Probability that the image is '{text}': {p:.3f}")
```

## Building & developing from source

**Note**: The following may give timeout errors due to the filesizes. If so, this can be fixed with poetry version 1.1.13 - see [this related issue.](https://github.com/python-poetry/poetry/issues/6009)

### Install, run, build and publish with Poetry

Install [Poetry](https://python-poetry.org/docs/)
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

To setup the project and create a virtual environment run the following command from the project's root directory.
```
poetry install
```

To build a source and wheel distribution of the library run the following command from the project's root directory.
```
poetry build
```

#### Instructions to publish the build artifacts for project maintainers

First, configure the upload API endpoint in Poetry:
```shell
poetry config repositories.onnx_clip https://gitlab.com/api/v4/projects/41150990/packages/pypi
```

With this setup you can now publish a package like so
```
poetry publish --repository onnx_clip -u <access_token_name> -p <access_token_key>
```
WARNING: Do not publish to the public pypi registry, e.g. always use the --repository option.
NOTE1: You must generate [an access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)
with scope set to api.  
NOTE2: The push will fail if there is already a package with the same version. You can increment the version using [poetry](https://python-poetry.org/docs/cli/#version)
```
poetry version
```
or by manually changing the version number in pyproject.toml.

## Help

Please let us know how we can support you: [earlyaccess@lakera.ai](mailto:earlyaccess@lakera.ai).

## LICENSE
See the [LICENSE](./LICENSE) file in this repository.

The `franz-kafka.jpg` is taken from [here](https://www.knesebeck-verlag.de/franz_kafka/p-1/270).