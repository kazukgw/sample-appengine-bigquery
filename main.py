import os
import json

from flask import Flask, request, jsonify
from google.cloud import bigquery
from google.oauth2 import service_account

app = Flask(__name__)

cred = '''\
{
  "type": "service_account",
}'''


@app.route('/read_from_bq')
def read_from_bq():
    cred_info = json.loads(cred)
    credentials = service_account.Credentials.from_service_account_info(cred_info)
    cli = bigquery.Client(credentials=credentials)
    results = list(cli.query_rows('select * from `kazukgw-prvt.binlog_stream.Raw` limit 100'))
    return jsonify({'results': results})
