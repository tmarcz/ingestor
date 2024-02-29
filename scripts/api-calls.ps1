# single start
curl -Method Post http://localhost:8000/driver/start/0001-0001 -H @{ "content-type" = "application/json"} -Body '{"name":"name1"}'
curl -Method Post http://localhost:8000/driver/start/0001-0001 -H @{ "content-type" = "application/json"} -InFile .\api-body.json

# parallel start
1..10 | ForEach-Object { Start-Job { curl -Method Post http://localhost:8000/driver/start/0001-0001 -H @{"content-type" = "application/json"} -Body '{"name":"name1"}' } } | Wait-Job | Receive-Job
