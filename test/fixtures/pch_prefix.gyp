{
  'targets': [
    {
      'target_name': 'pch_prefix',
      'type': 'executable',
      'sources': [ 'pch.cc' ],
      'xcode_settings': {
        'GCC_PREFIX_HEADER': 'pch.h',
        'GCC_PRECOMPILE_PREFIX_HEADER': 'YES',
      },
      # A prefix header is allowed to include generated headers, so the .gch has
      # to wait for this target's actions the same way its objects do.
      'actions': [
        {
          'action_name': 'make_header',
          'inputs': [],
          'outputs': [ '<(SHARED_INTERMEDIATE_DIR)/generated.h' ],
          'action': [ 'touch', '<(SHARED_INTERMEDIATE_DIR)/generated.h' ],
        },
      ],
    },
  ]
}
