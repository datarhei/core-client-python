from pydantic import BaseModel


class Alias(BaseModel):
    """
    api.Alias - a rewrite rule for the HTTP filesystems. A request whose path
    matches `pattern` is served with the content of `target`. Aliases are
    evaluated in list order; the first match applies.

    {
        "pattern": "^/live/(.+)\\.m3u8$",
        "target": "/memfs/$1/index.m3u8"
    }

    - pattern: regular expression matched against the requested path. It is
      also the ID of the alias (used by the /alias/rule endpoints).
    - target: absolute path to serve. Can reference capture groups of the
      pattern with $1, ${1} or ${name}.
    """

    pattern: str
    target: str
