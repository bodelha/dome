import React from 'react';
import { Box, Typography, TextField, Button, Grid } from '@mui/material';
import { useNavigate } from 'react-router-dom';

const Login = () => {
    const navigate = useNavigate();

    const handleLogin = (e) => {
        e.preventDefault();
        navigate('/home');
    };

    return (
        <Grid container sx={{ height: '100vh', width: '100%', margin: 0 }}>
            <Grid
                item
                xs={12}
                md={6}
                sx={{
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'center',
                    alignItems: 'center',
                    padding: 4,
                }}
            >
                <Typography variant="h5" sx={{ color: 'primary.main', fontFamily: 'Borel', position: 'absolute', top: 24, left: 24 }}>
                    Dome
                </Typography>

                <Typography variant="h4" gutterBottom sx={{ marginBottom: 2, textAlign: 'center' }}>
                    Bem-vindo de volta!
                </Typography>
                <Typography variant="body1" gutterBottom sx={{ marginBottom: 3, textAlign: 'center' }}>
                    Faça login na sua conta para continuar.
                </Typography>
                <form onSubmit={handleLogin} style={{ width: '100%', maxWidth: '400px' }}>
                    <TextField
                        label="Email"
                        variant="outlined"
                        fullWidth
                        margin="normal"
                        required
                        sx={{ marginBottom: 1 }}
                    />
                    <TextField
                        label="Senha"
                        variant="outlined"
                        type="password"
                        fullWidth
                        margin="normal"
                        required
                        sx={{ marginBottom: 3 }}
                    />
                    <Button type="submit" variant="contained" color="primary" fullWidth>
                        Login
                    </Button>
                </form>
            </Grid>

            <Grid item xs={12} md={6} sx={{ padding: 0 }}>
                <Box
                    component="img"
                    src="/ImagemLogin.jpg"
                    alt="Login"
                    sx={{
                        width: '100%',
                        height: '100%',
                        objectFit: 'cover',
                        display: 'block'
                    }}
                />
            </Grid>
        </Grid>
    );
};

export default Login;
