Date=$(date +%x_%H:%M:%S:%N | sed 's/\(:[0-9][0-9]\)[0-9]*$/\1/')

echo "============================================"
echo $Date
python ~/Documents/playground/happy-birthday-mate/main.py
echo "============================================"
