import {StyleSheet} from 'react-native';
import Colors from './colors';

const typography = StyleSheet.create({
  secondaryTitleText: {
    fontSize: 25,
  },
  titleText: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  errorText: {
    fontSize: 20,
    fontWeight: 'bold',
    padding: 16,
    textAlign: 'center',
  },
  guideText: {
    textDecorationLine: 'underline',
    fontSize: 20,
    marginHorizontal: 24,
    marginTop: 37,
  },
  itemText: {
    color: Colors.white,
    fontSize: 24,
  },
  buttonText: {
    fontSize: 15,
  },
});
export default typography;
