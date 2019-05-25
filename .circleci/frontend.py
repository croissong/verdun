CHANGE_CHECKER=./scripts/changed-since-last-commit.py
SUB_DIR=./src/api
if [[ `python3 ${CHANGE_CHECKER} ${SUB_DIR}` == "True" ]]; then
    # run unit tests against ${SUB_DIR}
fi
