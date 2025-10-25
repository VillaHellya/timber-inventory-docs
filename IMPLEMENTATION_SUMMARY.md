# 📋 REZUMAT COMPLET IMPLEMENTARE FIREBASE + ToS

**Data:** 25 Octombrie 2025
**Versiune:** 1.0.2+4
**Status:** ✅ COD COMPLET | ⏳ AȘTEPTARE SETUP FIREBASE

---

## ✅ CE AM IMPLEMENTAT (COD COMPLET)

### **1. Firebase Integration**

#### **Fișiere modificate:**
```
✅ pubspec.yaml
   - firebase_core: ^3.6.0
   - firebase_auth: ^5.3.1
   - cloud_firestore: ^5.4.4
   - url_launcher: ^6.3.1

✅ android/settings.gradle.kts
   - Google Services plugin v4.4.2

✅ android/app/build.gradle.kts
   - Google Services aplicat

✅ lib/main.dart
   - Firebase.initializeApp() la pornire
   - TosCheckScreen pentru verificare acceptare
   - Routing către /home după accept

✅ lib/core/services/tos_acceptance_service.dart (NOU)
   - Firebase Anonymous Auth automat
   - Logging în Firestore
   - Backup local în SharedPreferences
   - Link cu RevenueCat User ID
   - GDPR methods (export, revoke)

✅ lib/features/settings/presentation/screens/tos_acceptance_screen.dart (NOU)
   - UI complet pentru acceptare ToS
   - Disclaimer important (roșu)
   - Rezumat puncte cheie
   - Checkbox "Am citit și sunt de acord"
   - Link-uri către documente complete
   - Butoane Accept/Refuz
```

---

### **2. Flow Aplicație**

```
User deschide app
    ↓
Firebase.initializeApp()
    ↓
TosCheckScreen verifică: hasAcceptedTos()?
    ↓
    ├─ DA → ApvListScreen (home)
    │
    └─ NU → TosAcceptanceScreen
           ↓
           User citește + bifează checkbox
           ↓
           Click "Accept"
           ↓
           TosAcceptanceService.logAcceptance()
           ↓
           ├─ Firebase Anonymous Auth (dacă nu există)
           ├─ Salvare în Firestore: /tos_acceptances/{uid}
           └─ Backup local: SharedPreferences
           ↓
           Navigator → /home (ApvListScreen)
```

---

## ⏳ CE TREBUIE SĂ FACI TU

### **PARTEA 1: Setup Firebase Console (15 min)**

Vezi ghidul detaliat: **`FIREBASE_SETUP_INSTRUCTIONS.md`**

**Rezumat rapid:**
1. Creează Firebase Project: "Timber Inventory Pro"
2. Adaugă Android app: `com.forestry.timber_inventory`
3. Download `google-services.json` → copy în `android/app/`
4. Activează Authentication → Anonymous
5. Creează Firestore Database (eur3) + Security Rules

---

### **PARTEA 2: Actualizare Documente Legale (30 min)**

⚠️ **CRITICAL:** Privacy Policy și Terms TREBUIE actualizate înainte de Google Play!

#### **Privacy Policy - Ce trebuie adăugat:**

**Secțiune nouă 1.3: Date Firebase**
```html
<h3>1.3 Date Transmise către Firebase (Google)</h3>
<p>Pentru conformitate GDPR și audit trail legal, transmitem:</p>
<ul>
    <li>🔑 <strong>Firebase Anonymous User ID:</strong> Generat automat de Firebase</li>
    <li>📋 <strong>Versiune ToS/Privacy acceptată:</strong> ex: "1.0.2"</li>
    <li>⏰ <strong>Data/ora acceptării:</strong> Timestamp server Firebase</li>
    <li>📱 <strong>Versiune aplicație:</strong> ex: "1.0.2+4"</li>
    <li>💳 <strong>RevenueCat User ID:</strong> Pentru link cu subscripția (dacă există)</li>
</ul>

<div class="highlight">
    <strong>ℹ️ De ce Firebase?</strong><br>
    - ✅ Dovadă GDPR permanentă (chiar dacă dezinstalezi app)<br>
    - ✅ Servere Google EU (eur3 - Europe West)<br>
    - ✅ Sincronizare acceptare pe multiple dispozitive<br>
    - ✅ Audit trail pentru protecție juridică
</div>

<h4>Locație Stocare Firebase</h4>
<ul>
    <li>🌍 <strong>Cloud Firestore:</strong> Google Cloud (region: europe-west)</li>
    <li>🔒 <strong>Securitate:</strong> Row Level Security (RLS) - fiecare user vede doar datele proprii</li>
    <li>📅 <strong>Păstrare:</strong> Permanent (până la cerere GDPR ștergere)</li>
</ul>
```

**Secțiune nouă 1.4: Date Google AdMob**
```html
<h3>1.4 Date Colectate de Google AdMob</h3>
<p>Aplicația afișează reclame prin Google AdMob. Google colectează:</p>
<ul>
    <li>📱 <strong>Google Advertising ID (GAID):</strong> Identificator unic pentru reclame</li>
    <li>🌐 <strong>IP Address:</strong> Pentru geo-targeting reclame</li>
    <li>📊 <strong>Device Info:</strong> Model, OS version, limba</li>
    <li>🎯 <strong>Ad Interactions:</strong> Click-uri, view-uri reclame</li>
</ul>

<p><strong>⚠️ IMPORTANT:</strong> Google AdMob poate partaja datele cu advertiseri terți.</p>

<p><strong>Poți opta-out din reclame personalizate:</strong></p>
<ol>
    <li>Android Settings → Google → Ads</li>
    <li>Toggle "Opt out of Ads Personalization"</li>
</ol>

<p><strong>Google Privacy Policy:</strong>
<a href="https://policies.google.com/privacy" target="_blank">https://policies.google.com/privacy</a></p>
```

**Secțiune actualizată 3.1: Servicii Terțe**
```html
<h3>3.1 Servicii Terțe Utilizate</h3>
<ul>
    <li><strong>Firebase (Google):</strong> Logging acceptare ToS, Anonymous Authentication
        <br><small>Privacy Policy: <a href="https://firebase.google.com/support/privacy" target="_blank">https://firebase.google.com/support/privacy</a></small>
    </li>
    <li><strong>Google AdMob:</strong> Afișare reclame
        <br><small>Privacy Policy: <a href="https://policies.google.com/privacy" target="_blank">https://policies.google.com/privacy</a></small>
    </li>
    <li><strong>RevenueCat:</strong> Gestionare subscripții Pro
        <br><small>Privacy Policy: <a href="https://www.revenuecat.com/privacy" target="_blank">https://www.revenuecat.com/privacy</a></small>
    </li>
    <li><strong>Google Play Billing:</strong> Procesare plăți
        <br><small>Privacy Policy: <a href="https://policies.google.com/privacy" target="_blank">https://policies.google.com/privacy</a></small>
    </li>
</ul>
```

---

#### **Terms of Service - Ce trebuie adăugat:**

**Secțiune 6.2 actualizată: Limitare Răspundere**
```html
<h3>6.2 Limitare Despăgubiri</h3>
<p>În niciun caz, MAP Software - Mircea Popa NU va fi răspunzător pentru:</p>
<ul>
    <li>❌ Pierderi financiare cauzate de erori de calcul</li>
    <li>❌ Amenzi primite de la autorități (Garda Forestieră, APM) din cauza datelor greșite</li>
    <li>❌ Pierderea datelor din cauza dezinstalării, defectării telefon, etc.</li>
    <li>❌ Daune indirecte, întâmplătoare sau consecutive</li>
</ul>

<div class="highlight" style="background-color: #FFF3E0; border-left: 4px solid #FF6F00; padding: 20px; margin: 20px 0;">
    <h4 style="color: #FF6F00; margin-top: 0;">💰 PLAFON MAXIM DE RĂSPUNDERE</h4>
    <p><strong>Răspunderea maximă este limitată la MINIMUL dintre:</strong></p>
    <ul style="margin: 10px 0; line-height: 1.8;">
        <li>✅ Valoarea totală a subscripțiilor plătite în ultimele 6 luni, SAU</li>
        <li>✅ <strong style="color: #D32F2F; font-size: 1.2em;">150 lei (RON) per abonat</strong>, indiferent de numărul de incidente</li>
    </ul>

    <p><strong>Exemplu concret:</strong></p>
    <table style="width: 100%; border-collapse: collapse; margin: 10px 0;">
        <tr style="background-color: #FFF;">
            <th style="border: 1px solid #ddd; padding: 8px;">Scenariu</th>
            <th style="border: 1px solid #ddd; padding: 8px;">Suma Plătită (6 luni)</th>
            <th style="border: 1px solid #ddd; padding: 8px;">Răspundere Maximă</th>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">Plan lunar (€2 × 6 luni)</td>
            <td style="border: 1px solid #ddd; padding: 8px;">24 lei (~12 EUR)</td>
            <td style="border: 1px solid #ddd; padding: 8px;"><strong>24 lei</strong></td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">Plan anual (€15)</td>
            <td style="border: 1px solid #ddd; padding: 8px;">75 lei (~15 EUR)</td>
            <td style="border: 1px solid #ddd; padding: 8px;"><strong>75 lei</strong></td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">Plan anual × 2 ani</td>
            <td style="border: 1px solid #ddd; padding: 8px;">150 lei (~30 EUR)</td>
            <td style="border: 1px solid #ddd; padding: 8px;"><strong>150 lei</strong> (plafon)</td>
        </tr>
    </table>

    <p style="margin-top: 15px; font-style: italic; color: #666;">
        <strong>Notă:</strong> Chiar dacă ați plătit mai mult de 150 lei pe parcursul utilizării aplicației,
        răspunderea noastră nu va depăși niciodată 150 lei per utilizator, indiferent de natura sau numărul incidentelor.
    </p>
</div>

<p><strong>⚠️ Această limitare este conformă cu:</strong></p>
<ul>
    <li>📜 Codul Civil Român (art. 1350-1371 - Răspundere contractuală)</li>
    <li>🇪🇺 Directiva UE 2011/83/UE (Drepturile consumatorilor)</li>
    <li>⚖️ Jurisprudența CJUE (Limitări proporționale sunt valide)</li>
</ul>
```

---

## 📊 STRUCTURA DATELOR FIREBASE

### **Collection: `tos_acceptances`**

```javascript
/tos_acceptances/{firebase_anonymous_uid}/
{
  tos_version: "1.0.2",
  privacy_version: "1.0.2",
  app_version: "1.0.2+4",
  acceptance_timestamp: Timestamp(2025-10-25 14:32:15),
  revenuecat_user_id: "abc123xyz",  // Link cu subscripția
  platform: "android"
}
```

### **Security Rules (deja configurate în cod):**
```javascript
- User poate CREATE doar o singură dată (propria acceptare)
- User poate READ doar propria acceptare
- NU poate UPDATE/DELETE (acceptare permanentă)
```

---

## 🔐 GDPR COMPLIANCE

### **Date Colectate:**
1. ✅ **Firebase Anonymous UID** - generat automat, nu identifică persoana
2. ✅ **Versiuni ToS/Privacy** - pentru tracking modificări
3. ✅ **Timestamp** - dovadă când a acceptat
4. ✅ **RevenueCat ID** - link cu subscripția (opțional)

### **Baza Legală (GDPR Art. 6):**
- **Interes legitim (Art. 6.1.f):** Dovada consimțământului pentru apărare juridică
- **Executare contract (Art. 6.1.b):** Acceptarea ToS e necesară pentru folosirea app

### **Drepturile Utilizatorului:**
- **Drept la Acces:** `TosAcceptanceService.exportUserData()`
- **Drept la Ștergere:** `TosAcceptanceService.revokeAcceptance()` + Firestore update
- **Drept la Portabilitate:** Export JSON din Firestore Console

---

## 🎯 NEXT STEPS (În Ordine)

1. **[TU]** Configurează Firebase Console (15 min) - vezi `FIREBASE_SETUP_INSTRUCTIONS.md`
2. **[TU]** Copiază `google-services.json` în `android/app/`
3. **[TU]** Actualizează `privacy-policy.html` cu secțiunile Firebase + AdMob (30 min)
4. **[TU]** Actualizează `terms-of-service.html` cu plafon 150 lei (10 min)
5. **[TU]** Commit + push documente actualizate pe GitHub
6. **[AUTOMAT]** GitHub Pages va publica automat la:
   - `https://villahellya.github.io/timber-inventory-docs/privacy-policy.html`
   - `https://villahellya.github.io/timber-inventory-docs/terms-of-service.html`
7. **[TU]** Build APK: `flutter build apk --release`
8. **[TU]** Test pe telefon
9. **[TU]** Verifică în Firebase Console că acceptarea a fost loggată
10. **[TU]** Build AAB pentru Google Play: `flutter build appbundle --release`
11. **[TU]** Upload pe Google Play Console cu URL-uri actualizate

---

## 📞 SUPPORT & DEBUGGING

### **Verificare Rapidă:**
```bash
# 1. Check Firebase dependencies
flutter pub get

# 2. Check google-services.json
cat android/app/google-services.json | grep project_id

# 3. Clean build
flutter clean && flutter pub get

# 4. Build APK
flutter build apk --release

# 5. Install & test
adb install build/app/outputs/flutter-apk/app-release.apk
```

### **Loguri Firebase:**
```bash
adb logcat | grep -i firebase
adb logcat | grep -i firestore
```

---

© 2025 MAP Software - Mircea Popa
