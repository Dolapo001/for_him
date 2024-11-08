# build.sh

echo "  BUILD START"
# Install dependencies
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"  # Add poetry to PATH
pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear
echo "  BUILD END"
