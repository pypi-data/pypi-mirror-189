Contains files useful on PA and GS:
- protobuf definition AND compiled python
- custom mavlink frame code
- logger setup

# Protobuf messages in messages_pb2 are tracked by git, so when importing this repo as submodule # there is no need to compile protobuf.

# How to use this cool project

Poetry:
```poetry add git+ssh://git@gitlab.com:academic-aviation-club/sae-2023/advance_common.git```

Pip:
```pip install git+ssh://git@gitlab.com/academic-aviation-club/sae-2023/advance_common.git```

Notice the / instead of : for just pip, for me it only worked this way