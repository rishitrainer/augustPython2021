import stomp

host = "localhost"
port = 61613
dest = "/queue/SEDAP.MANUAL.CHECK"
conn = stomp.Connection(host_and_ports = [(host, port)])
conn.connect()
data = "Message {}"
for i in range(1, 100):
    conn.send(destination=dest, body=data.format(i), persistent='true')
print("Done!")
conn.disconnect()
