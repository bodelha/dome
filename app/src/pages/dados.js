import React from 'react';
import { Box, AppBar, Toolbar, Typography, Container, Link } from '@mui/material';
import PersonIcon from '@mui/icons-material/Person';
import AssessmentIcon from '@mui/icons-material/Assessment';
import IconButton from '@mui/material/IconButton';
import { useNavigate } from 'react-router-dom';

const Dados = () => {
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

                <Typography variant="h2" color='secondary.dark' fontWeight="light">
                   Dados da nossa aplicação:
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

export default Dados;
