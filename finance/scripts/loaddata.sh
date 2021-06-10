root=$(pwd)
fixtures_path=$root/data/raw_data

for fixture in $fixtures_path/*.tar.gz; do
  tar xvfz $fixture -C $fixtures_path
  fixture_json="${fixture%%.*}.json"
  set -o xtrace
  ./manage.py loaddata $fixture_json
  set +o xtrace
  rm $fixture_json
done
