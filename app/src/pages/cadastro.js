import React from 'react';
import { Typography, TextField, Button, Grid } from '@mui/material';
import { NavLink, useNavigate } from 'react-router-dom';

const Cadastro = () => {
    const navigate = useNavigate();

    const handleLogin = (e) => {
        e.preventDefault();
        navigate('/login');
    };

    return (
        <Grid
            container
            sx={{
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                height: '100vh',
                width: '100%',
            }}
        >
            <Grid
                item
                xs={12}
                md={6}
                sx={{
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'center',
                    alignItems: 'center',
                }}
            >
                <Typography variant="h5" sx={{ color: 'primary.main', fontFamily: 'Borel', position: 'absolute', top: 24, left: 24 }}>
                    Dome
                </Typography>

                <Typography variant="h4" gutterBottom sx={{ textAlign: 'center' }}>
                    Bem-vindo!
                </Typography>

                <NavLink to="/login" style={{ textDecoration: 'none' }}>
                    Possui conta? Clique aqui
                </NavLink>

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
                        sx={{ marginBottom: 1 }}
                    />
                    <TextField
                        label="Confirmar Senha"
                        variant="outlined"
                        type="password"
                        fullWidth
                        margin="normal"
                        required
                        sx={{ marginBottom: 3 }}
                    />
                    <Button type="submit" variant="contained" color="primary" fullWidth>
                        Cadastre-se
                    </Button>
                </form>
            </Grid>
        </Grid>
    );
};

export default Cadastro;
