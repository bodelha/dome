import React from 'react';
import { Box, AppBar, Toolbar, Typography, Container, Button, IconButton, Link } from '@mui/material';
import PersonIcon from '@mui/icons-material/Person';
import AssessmentIcon from '@mui/icons-material/Assessment';
import { useNavigate } from 'react-router-dom';

const Home = () => {
    const navigate = useNavigate();

    const handleNavigate = () => {
        navigate('/sobre');
    };

    const handleLoginNavigate = () => {
        navigate('/login');
    };

    const handleDataNavigate = () => {
        navigate('/dados');
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
                    <Box>
                        <IconButton
                            color="inherit"
                            sx={{ marginRight: 2, '&:hover': { backgroundColor: 'transparent' } }}
                            disableRipple
                            onClick={handleDataNavigate}
                        >
                            <AssessmentIcon sx={{ marginRight: 1 }} />
                            <Typography variant="body2">Dados</Typography>
                        </IconButton>
                        <IconButton color="inherit" onClick={handleLoginNavigate}>
                            <PersonIcon />
                        </IconButton>
                    </Box>
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

            <Container maxWidth="lg" sx={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
                <Box sx={{ paddingY: 4 }}>
                    <Typography variant="h2" color="primary" align="center" fontWeight="light" gutterBottom>
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
                    <Typography variant="h5" gutterBottom>
                        Visamos obter o melhor resultado para nossos usuários.
                    </Typography>
                    <Typography variant="body1" gutterBottom>
                        Esse projeto é feito para o PI (Projeto Interdisciplinar) da Fatec, feito como meio
                        avaliativo da faculdade, para saber mais clique no botão abaixo para ir para o nosso sobre:
                    </Typography>
                    <Box sx={{ display: 'flex', justifyContent: 'center', marginTop: 1 }}>
                        <Button variant="contained" color="primary" onClick={handleNavigate}>
                            Saiba mais
                        </Button>
                    </Box>
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
