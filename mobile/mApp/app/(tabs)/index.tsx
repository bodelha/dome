import React, { useState } from 'react';
import {
  StyleSheet,
  Text,
  View,
  TextInput,
  TouchableOpacity,
} from 'react-native';
import { useNavigation } from '@react-navigation/native';
import AsyncStorage from '@react-native-async-storage/async-storage';

type NavigationProps = {
  navigate: (screen: string) => void;
};

const Login: React.FC = () => {
  const [email, setEmail] = useState<string>('');
  const [password, setPassword] = useState<string>('');

  const navigation = useNavigation<NavigationProps>();

  const handleLogin = async (): Promise<void> => {
    try {
      const user = await AsyncStorage.getItem('user');
      if (!user) {
        alert('Nenhum usuário cadastrado');
        return;
      }
      const userJson = JSON.parse(user);
      if (userJson.email === email && userJson.password === password) {
        navigation.navigate('dados');
      } else {
        alert('E-mail ou senha inválidos!');
      }
    } catch (error) {
      console.error('Erro ao realizar o login:', error);
      alert('Ocorreu um erro, tente novamente.');
    }
  };

  const handleCadastro = (): void => {
    navigation.navigate('cadastro');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.iconText}>Dome</Text>
      <TextInput
        style={styles.input}
        placeholder="E-mail"
        value={email}
        onChangeText={setEmail}
        keyboardType="email-address"
        autoCapitalize="none"
      />
      <TextInput
        style={styles.input}
        placeholder="Senha"
        secureTextEntry={true}
        value={password}
        onChangeText={setPassword}
      />
      <TouchableOpacity style={styles.button} onPress={handleLogin}>
        <Text style={styles.buttonText}>Entrar</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button} onPress={handleCadastro}>
        <Text style={styles.buttonText}>Cadastrar</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#fff',
    paddingTop: 50,
  },
  iconText: {
    position: 'absolute',
    top: 30,
    left: 10,
    fontSize: 24,
    fontWeight: 'bold',
    color: '#02A676',
  },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 5,
    padding: 10,
    marginVertical: 5,
    width: '80%',
  },
  button: {
    backgroundColor: '#02A676',
    borderRadius: 5,
    padding: 10,
    width: '80%',
    alignItems: 'center',
    marginVertical: 5,
  },
  buttonText: {
    color: '#fff',
    fontWeight: 'bold',
    fontSize: 18,
  },
});

export default Login;
