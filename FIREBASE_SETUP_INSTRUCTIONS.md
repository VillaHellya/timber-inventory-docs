# 🔥 FIREBASE SETUP - Ghid Complet

**Data:** 25 Octombrie 2025
**Versiune App:** 1.0.2+4
**Status:** ⏳ IN PROGRESS - Necesită finalizare setup Firebase

---

## ✅ CE AM IMPLEMENTAT DEJA

### **1. Cod Flutter (COMPLET ✅)**
- ✅ `pubspec.yaml` - Dependințe Firebase adăugate
- ✅ `android/settings.gradle.kts` - Google Services plugin configurat
- ✅ `android/app/build.gradle.kts` - Google Services aplicat
- ✅ `lib/core/services/tos_acceptance_service.dart` - Service ToS complet
- ✅ `lib/features/settings/presentation/screens/tos_acceptance_screen.dart` - UI complet
- ✅ `lib/main.dart` - Verificare ToS la pornire

### **2. Documentație**
- ✅ Acest ghid de setup
- ⏳ Privacy Policy - trebuie actualizat (vezi mai jos)
- ⏳ Terms of Service - trebuie actualizat (vezi mai jos)

---

## 📋 CE TREBUIE SĂ FACI TU (15 minute)

### **STEP 1: Creează Firebase Project (5 min)**

1. **Accesează:** https://console.firebase.google.com/
2. **Click:** "Add project"
3. **Project name:** `Timber Inventory Pro`
4. **Google Analytics:** Dezactivează (toggle OFF)
5. **Click:** "Create project" → Așteaptă 30 sec

---

### **STEP 2: Adaugă Aplicația Android (3 min)**

1. **În Firebase Console, click pe iconița Android** 📱
2. **Android package name:**
   ```
   com.forestry.timber_inventory
   ```
   ⚠️ **EXACT acest nume** - nu schimba nimic!

3. **App nickname:** `Timber Inventory Pro` (opțional)
4. **SHA-1 certificate:** SKIP (las gol)
5. **Click:** "Register app"

---

### **STEP 3: Download google-services.json (1 min)**

1. **Click:** "Download google-services.json"
2. **Salvează fișierul**
3. **Copiază-l în:**
   ```
   C:\SOFT\FF_Calcul_VU\timber_inventory_pro\android\app\google-services.json
   ```

   ⚠️ **IMPORTANT:** Fișierul TREBUIE să fie în `android/app/`, NU în `android/`!

4. **Verifică:** Fișierul trebuie să conțină `"project_id": "timber-inventory-pro"` (sau similar)

---

### **STEP 4: Activare Firebase Authentication (2 min)**

1. **În Firebase Console:**
   - Sidebar stânga → **Build** → **Authentication**
   - Click **"Get started"**

2. **Sign-in method:**
   - Tab **"Sign-in method"**
   - Găsește **"Anonymous"**
   - Click pe el
   - Toggle **Enable** (ON/verde)
   - Click **"Save"**

✅ **Anonymous Auth activat!**

---

### **STEP 5: Activare Cloud Firestore (4 min)**

1. **În Firebase Console:**
   - Sidebar → **Build** → **Firestore Database**
   - Click **"Create database"**

2. **Security mode:**
   - Alege **"Start in production mode"**
   - Click **"Next"**

3. **Firestore location:**
   - Alege **"eur3 (europe-west)"** (cel mai aproape de România)
   - Click **"Enable"**
   - Așteaptă 1-2 minute

4. **Security Rules:**
   - După ce se creează, click tab **"Rules"**
   - **Înlocuiește TOT** cu codul de mai jos:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    // === ToS Acceptances Collection ===
    match /tos_acceptances/{userId} {

      // Allow CREATE doar dacă:
      // 1. User e autentificat (Anonymous)
      // 2. userId din path == auth.uid (nu poate crea pentru altcineva)
      // 3. Documentul NU există deja (nu poate re-accepta)
      allow create: if request.auth != null
                    && request.auth.uid == userId
                    && !exists(/databases/$(database)/documents/tos_acceptances/$(userId));

      // Allow READ doar pentru user propriu
      allow read: if request.auth != null
                  && request.auth.uid == userId;

      // INTERZIS update/delete (acceptarea e permanentă)
      allow update, delete: if false;
    }

    // DENY orice altceva
    match /{document=**} {
      allow read, write: if false;
    }
  }
}
```

   - Click **"Publish"**

✅ **Firestore configurat!**

---

## 🔨 BUILD & TEST

### **STEP 6: Install dependențe (1 min)**

```bash
cd C:\SOFT\FF_Calcul_VU\timber_inventory_pro
flutter pub get
```

---

### **STEP 7: Build APK (3 min)**

```bash
flutter build apk --release
```

**Output așteptat:**
```
✓ Built build\app\outputs\flutter-apk\app-release.apk (XX.X MB)
```

---

### **STEP 8: Test pe telefon (5 min)**

1. **Instalează APK:**
   ```bash
   adb install build\app\outputs\flutter-apk\app-release.apk
   ```

2. **Deschide aplicația**

3. **Ar trebui să vezi:**
   - Ecran "Termeni și Condiții"
   - Disclaimer roșu cu warning
   - Checkbox "Am citit și sunt de acord"
   - Butoane "Refuz" și "Accept"

4. **Testează:**
   - ✅ Click pe "Accept" → ar trebui să intre în aplicație
   - ✅ Închide aplicația și redeschide → NU mai cere ToS (a salvat acceptarea)

5. **Verifică în Firebase Console:**
   - Merg la **Firestore Database** → **tos_acceptances**
   - Ar trebui să vezi un document cu Firebase Anonymous UID
   - Conține: `tos_version`, `privacy_version`, `acceptance_timestamp`, etc.

---

## 🐛 TROUBLESHOOTING

### **Eroare: "google-services.json not found"**
```
FAILURE: Build failed with an exception.
* What went wrong:
File google-services.json is missing.
```

**Soluție:**
- Verifică că `google-services.json` este în `android/app/`
- NU în `android/` (directorul părinte)

---

### **Eroare: "Firebase not initialized"**
```
[ERROR:flutter/runtime/dart_vm_initializer.cc(41)] Unhandled Exception:
[core/no-app] No Firebase App '[DEFAULT]' has been created
```

**Soluție:**
- Verifică că `google-services.json` conține `"project_id"`
- Rulează `flutter clean` apoi `flutter pub get`
- Rebuilduiește APK-ul

---

### **Aplicația crahează imediat după pornire**

**Soluție:**
1. Conectează telefonul cu USB debugging
2. Rulează: `adb logcat | grep -i firebase`
3. Caută erori de tipul "FirebaseOptions" sau "google-services"
4. Verifică că `google-services.json` e valid (deschide-l în editor text)

---

### **ToS screen nu apare**

**Possible causes:**
1. **SharedPreferences are deja `tos_accepted=true`**
   - **Fix:** Dezinstalează complet app-ul și reinstalează

2. **Firebase Authentication nu e activat**
   - **Fix:** Vezi STEP 4 mai sus

---

## 📊 VERIFICARE FINALĂ

După setup complet, verifică:

- [ ] `google-services.json` în `android/app/`
- [ ] Firebase Authentication → Anonymous ENABLED
- [ ] Firestore Database creat (location: eur3)
- [ ] Firestore Rules publicate (vezi STEP 5)
- [ ] APK build-uit fără erori
- [ ] App instalată pe telefon
- [ ] ToS screen apare la prima pornire
- [ ] După Accept → intră în app
- [ ] După redeschidere → NU mai cere ToS
- [ ] Firestore Console → există document în `tos_acceptances`

---

## 🎯 NEXT STEPS

După ce Firebase funcționează:

1. **Actualizează Privacy Policy** (vezi `PRIVACY_POLICY_UPDATES.md`)
2. **Actualizează Terms of Service** (vezi `TERMS_OF_SERVICE_UPDATES.md`)
3. **Push documentele** pe GitHub Pages
4. **Build final** APK/AAB pentru Google Play

---

## 📞 SUPPORT

**Dacă ai probleme:**
1. Verifică acest ghid pas cu pas
2. Citește secțiunea Troubleshooting
3. Verifică Firebase Console → Logs (dacă există erori)

**Firebase Documentation:**
- https://firebase.google.com/docs/flutter/setup
- https://firebase.google.com/docs/auth/android/anonymous-auth
- https://firebase.google.com/docs/firestore/quickstart

---

© 2025 MAP Software - Mircea Popa
