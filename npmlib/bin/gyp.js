#!/usr/bin/env node
'use strict';

const { execFileSync } = require('child_process');
const path = require('path');

const { detect } = require('detect-python-interpreter');

const python = detect();

const args = process.argv.slice(2);
args.unshift(path.join(__dirname, '..', '..', 'gyp_main.py'));

try {
  execFileSync(python, args, {
    stdio: 'inherit',
  });
} catch (e) {
  process.exit(e.status || 9);
}
