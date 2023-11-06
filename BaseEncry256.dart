import 'dart:io';
import 'dart:convert';
import 'package:encrypt/encrypt.dart';
import 'package:pointycastle/asymmetric/api.dart';

//Resolve the encrypt package before running -> dart pub global activate encrypt
void main() {
  final plainText = 'Sam cannot can with the encryption methods';
  
  /* Salsa20 Encryption
  final key = Key.fromLength(32);
  final iv = IV.fromLength(8);
  final encrypter = Encrypter(Salsa20(key));

  final encrypted = encrypter.encrypt(plainText, iv: iv);
  final decrypted = encrypter.decrypt(encrypted, iv: iv);
  */

  /* Fernet Encryption
  final key = Key.fromUtf8('my32lengthsupersecretnooneknows1');
  final b64key = Key.fromUtf8(base64Url.encode(key.bytes).substring(0,32));
  final fernet = Fernet(b64key);
  final encrypter = Encrypter(fernet);

  final encrypted = encrypter.encrypt(plainText);
  final decrypted = encrypter.decrypt(encrypted);
  */

  /* RSA Encryption (asymmetric)
  final publicKey = await parseKeyFromFile<RSAPublicKey>(''); //insert pem file for public key
  final privateKey = await parseKeyFromFile<RSAPrivateKey>(''); //insert pem file for private key
  final encrypter = Encrypter(RSA(publicKey: publicKey, privateKey: privateKey));

  final encrypted = encrypter.encrypt(plainText);
  final decrypted = encrypter.decrypt(encrypted);
  */

  print(decrypted);
  print(encrypted.base64);
}