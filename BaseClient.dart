import 'package:socket_io/socket_io.dart';

main() {
  //Clientside Socket
  IO.Socket socket = IO.io('http://localhost:3000');
  socket.onConnect((_) {
    print('Socket Has Connected');
    socket.emit('msg', 'test');
  });
  socket.on('event', (data) => print(data));
  socket.onDisconnect((_) => print('disconnect'));
  socket.on('fromServer', (_) => print(_));
}