<?php

if (empty($argv[1])) {
  echo "usage: {$_SERVER['SCRIPT_NAME']} <file.in>\n";
  exit(1);
}

function translate($input) {
  $alphabet = "abcdefghijklmnopqrstuvwxyz";
  $mappings = "yhesocvxduiglbkrztnwjpfmaq";
  return strtr($input, $alphabet, $mappings);
}

$file = file_get_contents($argv[1]);
$lines = explode("\n", $file);
$T = trim(array_shift($lines));
for ($i = 0; $i < $T; ++$i) {
  $line = trim($lines[$i]);
  echo "Case #" . ($i+1) . ": " . translate($line) . "\n";
}
