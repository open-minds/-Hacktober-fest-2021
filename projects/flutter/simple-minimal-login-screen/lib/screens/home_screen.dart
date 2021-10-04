import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  Widget _iconWidget(String iconName) => Container(
        padding: EdgeInsets.all(8),
        child: SvgPicture.asset(iconName),
      );
  Widget _field(String hint, String iconName, bool isPasswordField) {
    return Row(
      children: [
        _iconWidget(iconName),
        SizedBox(
          width: 8,
        ),
        Container(
          decoration: BoxDecoration(
            borderRadius: BorderRadius.all(Radius.circular(16)),
            color: Colors.white.withOpacity(0.2),
          ),
          width: MediaQuery.of(context).size.width - 100,
          padding: EdgeInsets.all(6),
          margin: EdgeInsets.all(8),
          child: TextField(
            style: TextStyle(color: Colors.white),
            obscureText: isPasswordField,
            decoration: InputDecoration(
              hintText: hint,
              contentPadding: EdgeInsets.symmetric(vertical: 2, horizontal: 8),
              hintStyle: TextStyle(color: Colors.white.withOpacity(0.6)),
              border: InputBorder.none,
            ),
          ),
        )
      ],
    );
  }

  Widget _button(String label, Color color) {
    return InkWell(
        child: Container(
      width: MediaQuery.of(context).size.width - 20,
      height: 60,
      decoration: BoxDecoration(
          color: color, borderRadius: BorderRadius.all(Radius.circular(16))),
      child: Center(
        child: Text(
          label,
          style: TextStyle(
              fontSize: 20,
              color: Colors.white,
              fontWeight:
                  label == 'Create' ? FontWeight.bold : FontWeight.normal),
        ),
      ),
    ));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xff303249),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              SizedBox(
                height: 32,
              ),
              Text(
                'Create \nyour account',
                style: TextStyle(
                    height: 1,
                    fontSize: 40,
                    color: Colors.white,
                    fontWeight: FontWeight.bold),
              ),
              SizedBox(
                height: 32,
              ),
              Container(
                child: Column(
                  children: [
                    _field('Name', 'assets/icons/name.svg', false),
                    _field('Email', 'assets/icons/email.svg', false),
                    _field('Password', 'assets/icons/password.svg', true),
                  ],
                ),
              ),
              SizedBox(
                height: 32,
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.end,
                children: [
                  Container(
                    decoration: BoxDecoration(
                      color: Color(0xff1B91FF),
                      borderRadius: BorderRadius.all(
                        Radius.circular(16),
                      ),
                    ),
                    child: _iconWidget('assets/icons/email.svg'),
                  ),
                  SizedBox(
                    width: 8,
                  ),
                  _iconWidget('assets/icons/google.svg'),
                ],
              ),
              SizedBox(
                height: 32,
              ),
              _button('Create', Color(0xff1B91FF)),
              SizedBox(
                height: 32,
              ),
              _button('Login', Color(0xffFF25C2)),
            ],
          ),
        ),
      ),
    );
  }
}
