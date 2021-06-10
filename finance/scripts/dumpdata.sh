root=$(pwd)
fixtures_path=$root/data/raw_data
fixtures_name_list="taiex fundamentals company database stock holiday auth"
for fixtures_name in $fixtures_name_list; do
    fixtures_json="$fixtures_name.json"
    set -o xtrace
    ./manage.py dumpdata $fixtures_name --indent 2 > "$fixtures_json"
    set +o xtrace
    tar zcvf "$fixtures_path/$fixtures_name.tar.gz" "$fixtures_json"
    rm "$fixtures_json"
done
