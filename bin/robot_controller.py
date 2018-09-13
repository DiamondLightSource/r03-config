#make sure this is run in python3!!!

import json
import uarm
import socketserver


def accept(func,*args, **kwargs):
    return getattr(swift,func)(*args, **kwargs)

    
class RobotHandler(socketserver.StreamRequestHandler):

    def handle(self, *a):
        for line in self.rfile:
#            print(line)
            line = line.decode('utf-8')
            print(line)
            instruction=json.loads(line.strip())
            print(instruction)
            response=accept(instruction["func"],*instruction.get("args", []), **instruction.get("kwargs", {}))
            print(response)
            jresponse = json.dumps({'response':response})
            self.wfile.write(jresponse.encode())
ss = socketserver.ThreadingTCPServer(('localhost', 4446), RobotHandler)
swift = uarm.SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'})
if __name__ == "__main__":
    try:
        ss.serve_forever()
    except:
        print('shutting down')
    ss.shutdown()
    ss.socket.close()
    swift.disconnect()
