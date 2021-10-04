import React from 'react';
import {StyleSheet, Text, View, FlatList} from 'react-native';
import {useAppSelector} from '../redux/coffee_machine/hooks';
import {CoffeeMachineSliceType} from '../redux/coffee_machine/coffee_machine_slice';

import ExtraCard from '../components/extras_card';
import {Typography, ViewStyles} from '../styles';
import {Extra} from '../models';
export default function ExtraScreen() {
  const extras: Extra[] = useAppSelector(
    (state: CoffeeMachineSliceType) => state.pickedType.extra,
  );

  return (
    <View style={styles.mainView}>
      <View style={styles.titleView}>
        <Text style={styles.secondaryTitleText}>Select your extra's</Text>
      </View>
      <View style={styles.listView}>
        <FlatList
          keyExtractor={item => item._id.toString()}
          data={extras}
          renderItem={({item}) => <ExtraCard extra={item} />}
        />
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
  listView: {
    ...ViewStyles.listView,
  },
});
