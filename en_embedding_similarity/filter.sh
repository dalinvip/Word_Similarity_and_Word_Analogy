path=
nohup python -u filiter_vocab.py --vector ${path} --output ./embed/filtered.txt > log 2>&1 &
tail -f log

