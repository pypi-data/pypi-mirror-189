# BasketCase
Download images and videos from Instagram.

## Installation
Install it from [PyPI](https://pypi.org/project/basketcase/).

```sh
pip install basketcase
```

> This will put the executable `basketcase` on your PATH.

## Usage
```sh
basketcase -u "https://instagram.com/p/<post_id>"
```

> Downloaded resources will be stored in the current working directory (i.e. `$PWD/basketcase_{timestamp}/`).

To download from multiple URLs, create a text file (e.g. `basketcase.txt`) and populate it with resource URLs

```
https://instagram.com/p/<post_id>
https://instagram.com/reel/<reel_id>
https://instagram.com/<username>
```

```sh
basketcase -f ./basketcase.txt
```

### Supported URLs
| Supported URL | Description |
| --- | --- |
| `https://instagram.com/<username>` | User profile. Downloads stories from the past 24 hours. |
| `https://instagram.com/p/<post_id>` | Standard publication. |
| `https://instagram.com/reel/<reel_id>` | Reels movie |
| `https://www.instagram.com/stories/highlights/<highlight_id>/` | A collection of stories, or "highlights" |
| `https://www.instagram.com/s/<random_characters>` | A shorter type of URL |

### Authentication
1. Add a session cookie

```sh
basketcase --cookie <session_cookie_id> --cookie-name "my session cookie"
# Added session id: 1
```

2. Specify its identifier when downloading

```sh
basketcase -s 1
```

> List all available sessions with `basketcase -l`

## User data
Cookies and other application data are kept in `~/.basketcase`.

## Development setup
1. `cd` to the project root and create a virtual environment in a directory named `venv`, which is conveniently ignored in version control.
2. Install the dependencies.

```sh
pip install -r requirements.txt
```

3. Install this package in editable mode.

```sh
pip install -e .
```

### Package build and upload
1. Update the requirements list.

```sh
pip freeze --exclude-editable > requirements.txt
```

2. Increment the version on `pyproject.toml`.
3. Build the package.

```sh
hatch build
```

4. Commit and push the changes (and a new version tag) to the git repository.
5. Publish it.
```sh
hatch publish
```
