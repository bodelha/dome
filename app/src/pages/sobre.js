import React from 'react';
import { Box, AppBar, Toolbar, Typography, Container, Link } from '@mui/material';
import PersonIcon from '@mui/icons-material/Person';
import AssessmentIcon from '@mui/icons-material/Assessment';
import IconButton from '@mui/material/IconButton';
import { useNavigate } from 'react-router-dom';

const Sobre = () => {
    const navigate = useNavigate();

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

            <Container maxWidth="md" sx={{ flex: 1, padding: 2 }}>
                <Typography variant="h3" align='center' gutterBottom>
                    Sobre o Projeto Dome
                </Typography>
                <Typography variant="body1" paragraph>
                    O projeto Dome foi concebido para otimizar as condições de secagem de plantas em um ambiente controlado.
                    Por meio de sensores de Internet das Coisas (IoT), o sistema capta dados em tempo real sobre temperatura,
                    umidade e luminosidade, permitindo um monitoramento preciso e eficaz.
                </Typography>
                <Typography variant="body1" paragraph>
                    Nosso objetivo é aprimorar o processo de secagem, assegurando a máxima qualidade das plantas, enquanto
                    aumentamos a eficiência e a sustentabilidade da produção. Com o Dome, buscamos não apenas atender às
                    demandas do mercado, mas também promover práticas que respeitem o meio ambiente.
                </Typography>
                <Typography variant="h6" gutterBottom>
                    Tecnologias Utilizadas:
                </Typography>
                <ul>
                    <li>React.js para a construção da interface</li>
                    <li>Material UI para componentes de UI estilizados</li>
                    <li>MongoDB para o armazenamento dos dados</li>
                    <li>Node.js para a construção da API</li>
                </ul>
                <Typography variant="body1">
                    Se você deseja saber mais sobre o projeto ou tem alguma dúvida, não hesite em entrar em contato conosco!
                </Typography>
            </Container>

            <Box sx={{ borderTop: '1px solid', borderColor: 'primary.main', padding: 2, textAlign: 'center', color: 'primary.main' }}>
                <Typography variant="body2">
                    © {new Date().getFullYear()} Dome. Todos os direitos reservados.
                </Typography>
            </Box>
        </Box>
    );
};

export default Sobre;
