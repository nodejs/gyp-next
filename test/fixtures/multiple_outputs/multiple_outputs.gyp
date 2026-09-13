{
  'variables': {
    'mode%': 'default',
  },
  'targets': [
    {
      'target_name': 'multiple_outputs',
      'type': 'none',
      'actions': [
        {
          'action_name': 'generate',
          'inputs': [
            'generate.py',
            'input.txt',
          ],
          'outputs': [
            '<(SHARED_INTERMEDIATE_DIR)/first.txt',
            '<(SHARED_INTERMEDIATE_DIR)/second.txt',
          ],
          'action': [
            '<(python)',
            'generate.py',
            'input.txt',
            '<(SHARED_INTERMEDIATE_DIR)/runs.log',
            '<(mode)',
            '<@(_outputs)',
          ],
        },
      ],
    },
  ],
}
