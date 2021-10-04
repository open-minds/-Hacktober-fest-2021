import React from 'react';
import {Image, StyleSheet, Text, View} from 'react-native';
import {useAppDispatch} from '../redux/coffee_machine/hooks';
import {fetchCoffeeMachine} from '../redux/coffee_machine/thunks';

import {Typography, ViewStyles} from '../styles';
import {COFFEE_MACHINE_ID, COFFEE_MACHINE_NOT_FOUND} from '../utils/constants';
import AppButton from './app_button';

export default function ErrorComponents({error}: {error: string}) {
  const dispatch = useAppDispatch();
  return error === COFFEE_MACHINE_NOT_FOUND ? (
    <View style={styles.errorView}>
      <Image
        resizeMode="contain"
        style={styles.imgStyle}
        source={require('../assets/not_found_illustration.png')}
      />
      <Text style={{...Typography.errorText}}> {error}</Text>
    </View>
  ) : (
    <View style={styles.errorView}>
      <Image
        resizeMode="contain"
        style={styles.imgStyle}
        source={require('../assets/error_illustration.png')}
      />
      <Text style={{...Typography.errorText}}> {error}</Text>
      <AppButton
        title={'Try again'}
        onPress={() => dispatch(fetchCoffeeMachine(COFFEE_MACHINE_ID))}
      />
    </View>
  );
}
const styles = StyleSheet.create({
  errorView: {
    ...ViewStyles.errorView,
  },
  itemView: {
    ...ViewStyles.itemView,
  },
  circle: {
    ...ViewStyles.circle,
  },
  itemText: {
    ...Typography.itemText,
  },
  imgStyle: {
    ...ViewStyles.imgStyle,
  },
});
