import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { WebView } from 'react-native-webview';

export default function TabTwoScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.iconText}>Dome</Text>
      <WebView
        style={styles.webview}
        source={{
          uri: "https://app.powerbi.com/view?r=eyJrIjoiMTE5ZTU4NDYtOTc0OS00MDQyLTkwMzctMGYxZGVmODU2YTFmIiwidCI6ImNmNzJlMmJkLTdhMmItNDc4My1iZGViLTM5ZDU3YjA3Zjc2ZiIsImMiOjR9",
        }}
        javaScriptEnabled={true}
        domStorageEnabled={true}
        startInLoadingState={true}
        scalesPageToFit={true}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'flex-start',
  },
  iconText: {
    position: 'absolute',
    top: 20,
    left: 10,
    fontSize: 24,
    fontWeight: 'bold',
    color: '#02A676',
  },
  webview: {
    marginTop: 80,
    flex: 1,
    height: '100%',
    width: 400,
    borderWidth: 2,
    borderColor: '#D6D58E',
    borderRadius: 10,
  },
});
