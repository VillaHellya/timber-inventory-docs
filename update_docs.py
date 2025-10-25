#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script pentru actualizare ToS și Privacy Policy"""

import re

def update_terms_of_service():
    """Actualizare terms-of-service.html"""
    with open('terms-of-service.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Actualizare header identificare
    content = re.sub(
        r'<p><strong>Dezvoltator:</strong> MAP Software</p>\s*<p><strong>Ultima actualizare:</strong> Octombrie 2025</p>',
        '''<p><strong>Dezvoltator:</strong> Conform identificării în Google Play Console sub numele "MAP Software"</p>
        <p><strong>Identificare completă:</strong> Accesați profilul dezvoltatorului în Google Play Store pentru verificarea identității conform Regulamentului UE 2019/1150 (Platform-to-Business Relations)</p>
        <p><strong>Contact:</strong> map.dezvoltare@gmail.com</p>
        <p><strong>Ultima actualizare:</strong> 25 Octombrie 2025</p>''',
        content,
        flags=re.MULTILINE
    )

    # 2. Elimină linkuri clickable (doar email și URL-uri externe, nu interne)
    # Elimină tag-uri <a href="mailto:...">
    content = re.sub(
        r'<a href="mailto:map\.dezvoltare@gmail\.com">map\.dezvoltare@gmail\.com</a>',
        'map.dezvoltare@gmail.com',
        content
    )

    # 3. Elimină linkuri către privacy-policy.html și terms-of-service.html (doar în footer)
    content = re.sub(
        r'<a href="privacy-policy\.html">Politica de Confidențialitate</a>',
        'Politica de Confidențialitate (privacy-policy.html)',
        content
    )
    content = re.sub(
        r'<a href="terms-of-service\.html">Termeni și Condiții</a>',
        'Termeni și Condiții (terms-of-service.html)',
        content
    )

    # 4. Actualizare secțiune 13 Contact
    content = re.sub(
        r'(<div class="contact">.*?<p>\s*<strong>MAP Software</strong><br>\s*📧 Email: )<a href="mailto:[^"]+">([^<]+)</a>',
        r'\1\2',
        content,
        flags=re.DOTALL
    )

    with open('terms-of-service.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ terms-of-service.html actualizat")

def update_privacy_policy():
    """Actualizare privacy-policy.html"""
    with open('privacy-policy.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Elimină linkuri clickable email
    content = re.sub(
        r'<a href="mailto:map\.dezvoltare@gmail\.com">map\.dezvoltare@gmail\.com</a>',
        'map.dezvoltare@gmail.com',
        content
    )

    # Elimină linkuri interne
    content = re.sub(
        r'<a href="privacy-policy\.html">Politica de Confidențialitate</a>',
        'Politica de Confidențialitate (privacy-policy.html)',
        content
    )
    content = re.sub(
        r'<a href="terms-of-service\.html">Termeni și Condiții</a>',
        'Termeni și Condiții (terms-of-service.html)',
        content
    )

    # Actualizare ultima actualizare
    content = re.sub(
        r'Ultima actualizare:</strong> Octombrie 2025',
        r'Ultima actualizare:</strong> 25 Octombrie 2025',
        content
    )

    with open('privacy-policy.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ privacy-policy.html actualizat")

if __name__ == '__main__':
    update_terms_of_service()
    update_privacy_policy()
    print("\n🎉 Toate documentele au fost actualizate!")
