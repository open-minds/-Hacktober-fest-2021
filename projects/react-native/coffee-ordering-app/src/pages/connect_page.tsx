import React from 'react';
import {Image, StyleSheet, Text, TouchableOpacity, View} from 'react-native';
import {Typography, ViewStyles} from '../styles';

export default function IntroScreen({navigation}: {navigation: any}) {
  return (
    <View style={styles.mainView}>
      <View style={styles.titleView}>
        <Text style={styles.titleText}>Dark Roasted Beans</Text>
        <Text style={styles.secondaryTitleText}>Tap the machine to start</Text>
      </View>

      <View style={styles.ilusView}>
        <TouchableOpacity onPress={() => navigation.navigate('style')}>
          <Image source={require('../assets/connect_nfc.png')} />
        </TouchableOpacity>
        <Text style={styles.guideText}>How does this work</Text>
      </View>
    </View>
  );
}
const styles = StyleSheet.create({
  mainView: {
    ...ViewStyles.mainView,
  },
  titleView: {
    ...ViewStyles.titleView,
  },
  titleText: {
    ...Typography.titleText,
  },
  secondaryTitleText: {
    ...Typography.secondaryTitleText,
  },
  ilusView: {
    ...ViewStyles.ilusView,
  },
  guideText: {
    ...Typography.guideText,
  },
});
