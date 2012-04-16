<?php

if (empty($argv[1])) {
  echo "usage: {$_SERVER['SCRIPT_NAME']} <file.in>\n";
  exit(1);
}

$file = file_get_contents($argv[1]);
$lines = explode("\n", $file);
$T = trim(array_shift($lines));
for ($i = 0; $i < $T; $i++) {
  $inputs = explode(" ", trim(array_shift($lines)));
  $N = array_shift($inputs);
  $S = array_shift($inputs);
  $p = array_shift($inputs);
  $t = $inputs;

  $valid = $special = 0;
  foreach ($t as $score) {
    if ((($score + 2) / 3) >= $p) {
      $valid++;
    } else if (($score > 28) || ($score < 2)) {
      continue;
    } else if ($S && (($score + 4) / 3) >= $p){
      $S--;
      $valid++;
    }
  }
  echo "Case #" . ($i+1) . ": $valid\n";
}
