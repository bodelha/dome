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

type NavigationProp = {
    navigate: (screen: string) => void;
};

const Cadastro: React.FC = () => {
    const [email, setEmail] = useState<string>('');
    const [password, setPassword] = useState<string>('');

    const navigation = useNavigation<NavigationProp>();

    const handleCadastro = async () => {
        const user = {
            email,
            password,
        };
        await AsyncStorage.setItem('user', JSON.stringify(user));
        navigation.navigate('index');
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
            />
            <TextInput
                style={styles.input}
                placeholder="Senha"
                secureTextEntry={true}
                value={password}
                onChangeText={setPassword}
            />

            <TouchableOpacity style={styles.button} onPress={handleCadastro}>
                <Text style={styles.buttonText}>Cadastrar</Text>
            </TouchableOpacity>
        </View>
    );
};

const styles = StyleSheet.create({
    iconText: {
        position: 'absolute',
        top: 30,
        left: 10,
        fontSize: 24,
        fontWeight: 'bold',
        color: '#02A676',
      },
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: '#fff',
    },
    input: {
        borderWidth: 1,
        borderColor: '#ccc',
        borderRadius: 5,
        padding: 10,
        marginBottom: 10,
        width: '90%',
    },
    button: {
        backgroundColor: '#02A676',
        padding: 10,
        borderRadius: 5,
        width: '90%',
        alignItems: 'center',
    },
    buttonText: {
        color: '#fff',
        fontWeight: 'bold',
        fontSize: 20,
    },
});

export default Cadastro;
