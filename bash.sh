source venv/bin/activate
pytest test_one.py
exit_status=$?

if [ "${exit_status}" -ne 0 ];
then
    echo "EXIT ${exit_status}"
else
    echo "EXIT 0"
fi
