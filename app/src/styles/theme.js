import { createTheme } from '@mui/material/styles';

export const themeOptions = createTheme({
    palette: {
        mode: 'light',
        primary: {
            main: '#02A676',
        },
        secondary: {
            main: '#D6D58E',
        },
        divider: '#262626',
        background: {
            default: '#E2E2E2',
        },
        text: {
            primary: '#000000',
        },
    },
    typography: {
        fontFamily: '"Montserrat", "Helvetica", "Arial", sans-serif',
        h1: {
            fontWeight: 700,
        },
        h2: {
            fontWeight: 700,
        },
        h3: {
            fontWeight: 700,
        },
        body1: {
            fontWeight: 400,
        },
        body2: {
            fontWeight: 400,
        },
    },
    components: {
        MuiAppBar: {
            styleOverrides: {
                colorInherit: {
                    backgroundColor: '#689f38',
                    color: '#fff',
                },
            },
        },
    },
    shape: {
        borderRadius: 4,
    },
    spacing: 8,
});

export default themeOptions;
