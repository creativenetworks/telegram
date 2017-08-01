#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2017
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
import json

import pytest

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


@pytest.fixture(scope='class')
def inline_keyboard_markup():
    return InlineKeyboardMarkup(TestInlineKeyboardMarkup.inline_keyboard)


class TestInlineKeyboardMarkup:
    inline_keyboard = [[
        InlineKeyboardButton(text='button1', callback_data='data1'),
        InlineKeyboardButton(text='button2', callback_data='data2')
    ]]

    def test_send_message_with_inline_keyboard_markup(self, bot, chat_id, inline_keyboard_markup):
        message = bot.send_message(
            chat_id,
            'Testing InlineKeyboardMarkup',
            reply_markup=inline_keyboard_markup)

        assert message.text == 'Testing InlineKeyboardMarkup'

    def test_de_json(self, bot, inline_keyboard_markup):
        json_dict = {
            'inline_keyboard': [[
                self.inline_keyboard[0][0].to_dict(),
                self.inline_keyboard[0][1].to_dict()
            ]],
        }
        inline_keyboard_markup_json = InlineKeyboardMarkup.de_json(json_dict, bot)

        assert inline_keyboard_markup_json.to_dict() == inline_keyboard_markup.to_dict()

    def test_to_json(self, inline_keyboard_markup):
        json.loads(inline_keyboard_markup.to_json())

    def test_to_dict(self, inline_keyboard_markup):
        inline_keyboard_markup_dict = inline_keyboard_markup.to_dict()

        assert isinstance(inline_keyboard_markup_dict, dict)
        assert inline_keyboard_markup_dict['inline_keyboard'] == [
            [
                self.inline_keyboard[0][0].to_dict(),
                self.inline_keyboard[0][1].to_dict()
            ]
        ]
