import {
  StyleSheet,
  Text,
} from 'react-native';

export default function TabTwoScreen() {
  return (
    <>
    <Text style={styles.iconText}>Dome</Text>
    </>
  );
}

const styles = StyleSheet.create({
  iconText: {
    position: 'absolute',
    top: 30,
    left: 10,
    fontSize: 24,
    fontWeight: 'bold',
    color: '#02A676',
  },
  headerImage: {
    color: '#808080',
    bottom: -90,
    left: -35,
    position: 'absolute',
  },
  titleContainer: {
    flexDirection: 'row',
    gap: 8,
  },
});
