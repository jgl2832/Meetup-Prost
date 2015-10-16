#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple

Preset = namedtuple('Preset', 'name, language, description, display_name, etymology')

presets = [
			Preset(name=u"prost", display_name="Prost", language=u"German", etymology="""
					Latin pro ("for"), + sit ("may it be"): literally "may it be for (you)", "may it benefit (you)". Compare prosit.
				""", description="""
					<h3>Interjection</h3>
					<h4>prost!</h4>
					<ol><li>the usual toast when drinking alcohol; cheers</li></ol>
				"""),
			Preset(name=u"proost", display_name="Proost", language=u"Dutch", etymology=u"""
					from Latin prosit - may it be good (i.e., for you)), or "(op je) gezondheid" ((to your) health); in Belgium: schol (from Scandinavian) or santé (from the French
				""", description="""
					<h3>Interjection</h3>
					<h4>proost</h4>
					<ol><li>cheers (toast when drinking)</li></ol>
				"""),
			Preset(name=u"건배", display_name=u"건배", language=u"Korean", etymology=u"""
					gunbae, lit. "Dry the glass", similar to "bottoms up" in English. Sino-Korean word from 乾杯
				""", description=u"""
					<h3>Pronounciation</h3>
					<ul><li>IPA: /kʌ̹nbɛ̝/</li><li>Phonetic hangeul: 건배</li><li>Romanization: geonbae</li></ul>
				"""),
			Preset(name=u"kanpai", display_name=u"乾杯", language=u"Japanese", etymology=u"""
					kanpai, lit. "Dry the glass", similar to "bottoms up" in English. From Chinese
				""", description=u"""
					<h3>Interjection</h3>
					<p>乾杯 (hiragana かんぱい, romaji kanpai)</p>
					<ol><li>cheers; common toast. Idiomatically, bottoms up</li></ol>
				"""),
			Preset(name=u"saúde", display_name=u"Saúde", language=u"Portugese", etymology=u"""
					From Old Portuguese saude, from Latin salūtem, accusative singular of salūs (“health”).
				""",
				description=u"""
					<h3>Pronounciation</h3>
					<ul>
						<li>(Brazil) IPA: /sa.ˈu.d͡ʒi/</li>
						<li>(South Brazil) IPA: /sa.ˈu.de/</li>
						<li>(Portugal) IPA: /sɐ.ˈu.ðɨ/</li>
						<li>Hyphenation: sa‧ú‧de</li>
						<li>Rhymes: -udʒi</li>
					</ul>
					<h3>Interjection</h3>
					<h4>saúde</h4>
					<ol><li>cheers (toast when drinking)</li><li>gesundheit; bless you (said to someone who has just sneezed)</li></ol>
				"""),
		]

presets_by_name = {p.name: p for p in presets}
"""
presets = [
			u"proost", # dutch 
			u"かんぱい", # japanese (hiragana)
			u"sláinte", # irish
			u"فى صحتك", # arabic (egypt)
			u"santé", # french
			u"À la vôtre", # french
			u"salut", # catalan
			u"Skál", # icelandic
			u"Skål", # norwegian/swedish
			u"Salute", # italian
			u"Saúde", # portugese
			u"Mabuhay", # filipino
			u"cheers", # english
			u"salud", # spanish
		]
"""
