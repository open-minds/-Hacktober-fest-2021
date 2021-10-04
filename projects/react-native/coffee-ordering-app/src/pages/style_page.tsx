import React, {useEffect} from 'react';
import {
  StyleSheet,
  Text,
  View,
  FlatList,
  TouchableOpacity,
  ActivityIndicator,
} from 'react-native';

import {
  COFFEE_MACHINE_ID,
  FETCHING_COFFEE,
  FETCHING_COFFEE_FAILURE,
  FETCHING_COFFEE_IDLE,
  FETCHING_COFFEE_SUCCESS,
} from '../utils/constants';

import {fetchCoffeeMachine} from '../redux/coffee_machine/thunks';
import {pickCoffeeType} from '../redux/coffee_machine/coffee_machine_slice';
import {useAppDispatch, useAppSelector} from '../redux/coffee_machine/hooks';
import {Colors, Typography, ViewStyles} from '../styles';
import ErrorComponents from '../components/error_components';
import {Type} from '../models';

export default function StyleScreen({navigation}: {navigation: any}) {
  const state = useAppSelector(stat => stat);
  const postStatus = state.status;
  const coffies = state.coffeeMachine.types;
  const error = state.error;
  const dispatch = useAppDispatch();
  useEffect(() => {
    if (postStatus === FETCHING_COFFEE_IDLE) {
      dispatch(fetchCoffeeMachine(COFFEE_MACHINE_ID));
    }
  }, [postStatus, dispatch]);
  const renderItem = ({item}: {item: Type}) => (
    <TouchableOpacity
      onPress={() => {
        dispatch(pickCoffeeType(item));
        navigation.navigate('size');
      }}>
      <View style={styles.itemView}>
        <View style={styles.circle} />
        <Text style={styles.itemText}>{item.name}</Text>
      </View>
    </TouchableOpacity>
  );

  let content;
  switch (postStatus) {
    case FETCHING_COFFEE_IDLE:
      content = <View />;
      break;
    case FETCHING_COFFEE:
      content = <ActivityIndicator size="large" color={Colors.lightGreen} />;
      break;
    case FETCHING_COFFEE_FAILURE:
      content = <ErrorComponents error={error} />;
      break;
    case FETCHING_COFFEE_SUCCESS:
      content = (
        <FlatList
          keyExtractor={item => item._id.toString()}
          data={coffies}
          renderItem={renderItem}
        />
      );
      break;
    default:
      content = <View />;
      break;
  }

  return (
    <View style={styles.mainView}>
      <View style={styles.titleView}>
        <Text style={styles.titleText}>Brew with Lex</Text>
        <Text style={styles.secondaryTitleText}>Select your style</Text>
      </View>
      <View style={styles.listView}>{content}</View>
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
  guideText: {
    ...Typography.guideText,
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
});
