import React from 'react';
import { Box, AppBar, Toolbar, Typography, Container, Grid, Card, CardContent, Button, IconButton, Link } from '@mui/material';
import PersonIcon from '@mui/icons-material/Person';
import { useNavigate } from 'react-router-dom';

const Home = () => {
    const navigate = useNavigate();

    const handleNavigate = () => {
        navigate('/sobre');
    };

    const handleLoginNavigate = () => {
        navigate('/login');
    };

    return (
        <Box sx={{ backgroundColor: 'background.default', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
            <AppBar position="static" color="primary" sx={{ boxShadow: 'none' }}>
                <Toolbar sx={{ display: 'flex', justifyContent: 'space-between', height: '64px', paddingY: 0 }}>
                    <Link href="/" color="inherit" underline="none">
                        <Typography
                            variant="h5"
                            color="inherit"
                            sx={{
                                fontFamily: 'Borel',
                                margin: 0,
                                marginBottom: '-16px',
                                cursor: 'pointer',
                            }}
                        >
                            Dome
                        </Typography>
                    </Link>
                    <IconButton color="inherit" sx={{ lineHeight: '64px' }} onClick={handleLoginNavigate}>
                        <PersonIcon />
                    </IconButton>
                </Toolbar>
            </AppBar>

            <Box
                component="img"
                src="/ImagemHome.jpg"
                alt="ImgHome"
                sx={{
                    width: '100%',
                    height: 'auto',
                    maxHeight: '600px',
                    objectFit: 'cover',
                }}
            />

            <Container maxWidth="md" sx={{ flex: 1 }}>
                <Box sx={{ padding: 2 }}>
                    <Typography variant="h1" align='center' fontWeight={'light'} gutterBottom>
                        Monitoramento da secagem
                    </Typography>
                    <Typography variant="body1">
                        O projeto Dome visa monitorar as condições internas e externas do domo de secagem de plantas.
                        Nele, você poderá acompanhar e analisar os seguintes dados:
                    </Typography>
                    <ul>
                        <li>Temperatura (interna e externa)</li>
                        <li>Umidade (interna e externa)</li>
                        <li>Luminosidade</li>
                    </ul>
                </Box>

                <Grid container spacing={4}>
                    {['Temperatura', 'Umidade', 'Luminosidade'].map((variable) => (
                        <Grid item xs={12} sm={4} key={variable}>
                            <Card sx={{ backgroundColor: 'secondary.main' }}>
                                <CardContent>
                                    <Typography variant="h6" gutterBottom sx={{ color: 'secondary.dark' }}>
                                        {variable}
                                    </Typography>
                                    <Typography variant="body2" sx={{ color: 'secondary.dark' }}>
                                        Dados detalhados sobre o(a) {variable} do domo.
                                    </Typography>
                                </CardContent>
                            </Card>
                        </Grid>
                    ))}
                </Grid>

                <Box sx={{ padding: 2, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                    <Typography variant="h5" gutterBottom>
                        Visamos obter o melhor resultado para nossos usuários.
                    </Typography>
                    <Typography variant="body1" gutterBottom>
                        Esse projeto é feito para o PI (Projeto Interdisciplinar) da Fatec para saber mais
                        clique no botão abaixo para ir para o nosso sobre:
                    </Typography>
                    <Button variant="contained" color="primary" onClick={handleNavigate}>
                        Saiba mais
                    </Button>
                </Box>
            </Container>

            <Box sx={{ borderTop: '1px solid', borderColor: 'primary.main', padding: 2, textAlign: 'center', color: 'primary.main' }}>
                <Typography variant="body2">
                    © {new Date().getFullYear()} Dome. Todos os direitos reservados.
                </Typography>
            </Box>
        </Box>
    );
};

export default Home;
