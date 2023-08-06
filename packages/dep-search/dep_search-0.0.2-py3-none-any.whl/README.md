## API-Search dependency wrapper

Contains shared library wrapper with schemas and interfaces only.

#### For build new and publish:
```
$ poetry build
$ poetry publish
```

#### For third-party projects:
``` 
# include in project:
$ poetry add dep-search
```

```
# Example usage:

from dep-search import Search, op

# ...

search = Search(url=url, client=client, token=user_token)
tags = await searcher.tags(
    expression=op.Eq(field='meta.pk', value=tag_pk),
    lang='ru',
    limit=10,
    page=1,
)

assert tags.count == 1
assert tags.total == len(state_build.persistent['Tag'])
assert tags.items[0].meta.pk == tag_pk
assert tags.items[0].meta.lang == 'ru'

```

Have a fun!
