# Luck xit ofc / sebasxit ✅️

import os
import sys
import time
import subprocess
import importlib.util
from threading import Thread

# --- Lista de módulos (Nombre de importación : Nombre en Pip) ---
REQUIRED_MODULES =[
    ("requests", "requests"),
    ("httpx", "httpx"),
    ("google.protobuf", "protobuf"),
    ("Crypto", "pycryptodome"),
    ("jwt", "PyJWT"),
    ("urllib3", "urllib3"),
    ("protobuf_decoder", "protobuf-decoder"),
    ("pytz", "pytz"),
    ("aiohttp", "aiohttp"),
    ("cfonts", "python-cfonts"),
    ("google_play_scraper", "google-play-scraper")
]

# Códigos de color
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
WHITE = "\033[97m"
RESET = "\033[0m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(f"{CYAN}")
    print(" ██╗     ██╗   ██╗ ██████╗██╗  ██╗    ██╗  ██╗██╗████████╗")
    print(" ██║     ██║   ██║██╔════╝██║ ██╔╝    ╚██╗██╔╝██║╚══██╔══╝")
    print(" ██║     ██║   ██║██║     █████╔╝      ╚███╔╝ ██║   ██║   ")
    print(" ██║     ██║   ██║██║     ██╔═██╗      ██╔██╗ ██║   ██║   ")
    print(" ███████╗╚██████╔╝╚██████╗██║  ██╗    ██╔╝ ██╗██║   ██║   ")
    print(" ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝   ╚═╝   ")
    print(f"{RESET}          {WHITE}--- SISTEMA PRE-INSTALADOR ---{RESET}\n")

class Loader:
    def __init__(self):
        self.stop = False

    def animate(self, message):
        chars =["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        i = 0
        while not self.stop:
            sys.stdout.write(f"\r {YELLOW}{chars[i % len(chars)]}{RESET} {message}...")
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1

def install_modules():
    clear()
    banner()
    
    for import_name, pip_name in REQUIRED_MODULES:
        # Comprobar si el módulo existe
        spec = importlib.util.find_spec(import_name)
        
        if spec is None:
            # Si no existe, se instalará mostrando una animación de carga
            loader = Loader()
            t = Thread(target=loader.animate, args=(f"Instalando {pip_name}",))
            t.start()
            
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name], 
                                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                loader.stop = True
                t.join()
                print(f"\r {GREEN}✓{RESET} {pip_name.ljust(25)} {GREEN}[ÉXITO]{RESET}")
            except:
                loader.stop = True
                t.join()
                print(f"\r {RED}✗{RESET} {pip_name.ljust(25)} {RED}[FALLÓ]{RESET}")
        else:
            # Si ya está instalado
            print(f" {GREEN}✓{RESET} {pip_name.ljust(25)} {WHITE}[YA INSTALADO]{RESET}")
            time.sleep(0.05)

    print(f"\n{CYAN}Todos los sistemas están listos.{RESET}")
    time.sleep(1)
    clear()

# Esto se ejecutará al inicio del script
if __name__ == "__main__":
    install_modules()

# ---------------------------------------------------------------- #
# Script Principal
# ---------------------------------------------------------------- #

import requests, os, json, binascii, time, urllib3, base64, datetime, re, socket, ssl, asyncio, aiohttp, random, traceback
from protobuf_decoder.protobuf_decoder import Parser
from ARIYAN import *
from ARIYAN2 import *
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from MXARIYAN import DEcwHisPErMsG_pb2, MajoRLoGinrEs_pb2, PorTs_pb2, MajoRLoGinrEq_pb2
import google.protobuf.json_format as json_format

# =====================[ COMPROBACIÓN DE PERMISOS DE GITHUB ] =====================
def check_permission():
    print(f"{YELLOW}Comprobando permisos del servidor... Por favor, espera.{RESET}")
    url = "https://raw.githubusercontent.com/Ariyan20267/All-bot-controller/refs/heads/main/levelup.txt"
    try:
        # Tiempo de espera de 5 segundos, si no hay internet irá a error
        response = requests.get(url, timeout=5)
        text = response.text.strip().upper()
        
        if "ON" in text:
            print(f"{GREEN}¡Permiso Concedido! Iniciando Bot...{RESET}\n")
            time.sleep(1)
        else:
            print(f"{RED}¡Permiso Denegado! El Bot ha sido APAGADO por el Administrador.{RESET}")
            sys.exit()
            
    except requests.exceptions.RequestException:
        # Si estás offline o no hay conexión a internet
        print(f"{RED}¡Error de conexión! No hay internet.\nDebes estar en línea para ejecutar este bot. ¡No se permite el bypass sin conexión!{RESET}")
        sys.exit()
# =======================================================================

def rot13(text):
    result = ""
    for c in text:
        if 'a' <= c <= 'z':
            result += chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            result += chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += c
    return result

LEVEL_UP = rot13("EXP7868NFE NJM")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

async def SEndPacKeT(ChaT, OnLinE, TypE, PacKeT):
    if TypE == 'ChaT' and ChaT:
        ChaT.write(PacKeT)
        await ChaT.drain()
    elif TypE == 'OnLine' and OnLinE:
        OnLinE.write(PacKeT)
        await OnLinE.drain()

async def GeNeRaTeAccEss(uid, password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": await Ua(),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close"
    }
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("open_id"), data.get("access_token")
            return None, None

online_writer = None
whisper_writer = None
login_url, ob, version = AuToUpDaTE()
Hr = {
    'User-Agent': Uaa(),
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'Expect': "100-continue",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': ob
}
CURRENT_BOT_UID = None
region = 'IN'

async def encrypted_proto(encoded_hex):
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(encoded_hex, AES.block_size)
    encrypted_payload = cipher.encrypt(padded_message)
    return encrypted_payload

async def EncRypTMajoRLoGin(open_id, access_token):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = 1
    major_login.client_version = version
    major_login.system_software = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
    major_login.system_hardware = "Handheld"
    major_login.telecom_operator = "Verizon"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1920
    major_login.screen_height = 1080
    major_login.screen_dpi = "280"
    major_login.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    major_login.memory = 3003
    major_login.gpu_renderer = "Adreno (TM) 640"
    major_login.gpu_version = "OpenGL ES 3.1 v1.46"
    major_login.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    major_login.client_ip = "223.191.51.89"
    major_login.language = "es"
    major_login.open_id = open_id
    major_login.open_id_type = "4"
    major_login.device_type = "Handheld"
    memory_available = major_login.memory_available
    memory_available.version = 55
    memory_available.hidden_value = 81
    major_login.access_token = access_token
    major_login.platform_sdk_id = 1
    major_login.network_operator_a = "Verizon"
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    major_login.external_storage_total = 36235
    major_login.external_storage_available = 31335
    major_login.internal_storage_total = 2519
    major_login.internal_storage_available = 703
    major_login.game_disk_storage_available = 25010
    major_login.game_disk_storage_total = 26628
    major_login.external_sdcard_avail_storage = 32992
    major_login.external_sdcard_total_storage = 36235
    major_login.login_by = 3
    major_login.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
    major_login.reg_avatar = 1
    major_login.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
    major_login.channel_type = 3
    major_login.cpu_type = 2
    major_login.cpu_architecture = "64"
    major_login.client_version_code = "2019118695"
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 16383
    major_login.login_open_id_type = 4
    major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWAUOUgsvA1snWlBaO1kFYg=="
    major_login.loading_time = 13564
    major_login.release_channel = "android"
    major_login.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
    major_login.android_engine_init_flag = 110009
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    string = major_login.SerializeToString()
    return await encrypted_proto(string)

async def MajorLogin(payload):
    url = f"{login_url}MajorLogin"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200:
                return await response.read()
            return None

async def GetLoginData(base_url, payload, token):
    url = f"{base_url}/GetLoginData"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    Hr['Authorization'] = f"Bearer {token}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200:
                return await response.read()
            return None

async def DecRypTMajoRLoGin(data):
    proto = MajoRLoGinrEs_pb2.MajorLoginRes()
    proto.ParseFromString(data)
    return proto

async def DecRypTLoGinDaTa(data):
    proto = PorTs_pb2.GetLoginData()
    proto.ParseFromString(data)
    return proto

async def DecodeWhisperMessage(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = DEcwHisPErMsG_pb2.DecodeWhisper()
    proto.ParseFromString(packet)
    return proto

async def xAuThSTarTuP(TarGeT, token, timestamp, key, iv):
    uid_hex = hex(TarGeT)[2:]
    uid_length = len(uid_hex)
    encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_account_token = token.encode().hex()
    encrypted_packet = await EnC_PacKeT(encrypted_account_token, key, iv)
    encrypted_packet_length = hex(len(encrypted_packet) // 2)[2:]
    if uid_length == 9:
        headers = '0000000'
    elif uid_length == 8:
        headers = '00000000'
    elif uid_length == 10:
        headers = '000000'
    elif uid_length == 7:
        headers = '000000000'
    else:
        headers = '0000000'
    return f"0115{headers}{uid_hex}{encrypted_timestamp}00000{encrypted_packet_length}{encrypted_packet}"

async def join_teamcode_packet(team_code, key, iv, region):
    fields = {
        1: 4,
        2: {
            4: bytes.fromhex("01090a0b121920"),
            5: str(team_code),
            6: 6,
            8: 1,
            9: {2: 800, 6: 11, 8: "1.111.1", 9: 5, 10: 1}
        }
    }
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

async def start_auto_packet(key, iv, region):
    fields = {1: 9, 2: {1: 12480598706}}
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

async def leave_squad_packet(key, iv, region):
    fields = {1: 7, 2: {1: 12480598706}}
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

auto_start_running = False
stop_auto = False
auto_start_task = None
start_spam_duration = 18
wait_after_match = 5
start_spam_delay = 0.1

async def auto_start_loop(team_code, uid, chat_id, chat_type, key, iv, region):
    global auto_start_running, stop_auto
    while not stop_auto:
        try:
            join_pkt = await join_teamcode_packet(team_code, key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_pkt)
            await asyncio.sleep(2)

            start_pkt = await start_auto_packet(key, iv, region)
            end_time = time.time() + start_spam_duration
            while time.time() < end_time and not stop_auto:
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', start_pkt)
                await asyncio.sleep(start_spam_delay)

            if stop_auto:
                break

            waited = 0
            while waited < wait_after_match and not stop_auto:
                await asyncio.sleep(1)
                waited += 1
            if stop_auto:
                break

            leave_pkt = await leave_squad_packet(key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_pkt)
            await asyncio.sleep(2)

        except Exception as e:
            print(f"[AUTO] Error: {e}")
            break
    auto_start_running = False
    stop_auto = False

async def stop_auto_loop():
    global auto_start_running, stop_auto, auto_start_task
    stop_auto = True
    if auto_start_task and not auto_start_task.done():
        auto_start_task.cancel()
        try:
            await auto_start_task
        except asyncio.CancelledError:
            pass
    auto_start_running = False

async def safe_send_message(chat_type, message, target_uid, chat_id, key, iv, max_retries=3):
    for attempt in range(max_retries):
        try:
            P = await SEndMsG(chat_type, message, target_uid, chat_id, key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
            return True
        except Exception:
            if attempt < max_retries - 1:
                await asyncio.sleep(0.5)
    return False

async def TcPOnLine(ip, port, jwt_token, bot_uid, key, iv, AutHToKen, reconnect_delay=0.5):
    global online_writer
    while True:
        try:
            reader, writer = await asyncio.open_connection(ip, int(port))
            online_writer = writer
            writer.write(bytes.fromhex(AutHToKen))
            await writer.drain()
            while True:
                data = await reader.read(9999)
                if not data:
                    break
            online_writer.close()
            await online_writer.wait_closed()
            online_writer = None
        except Exception as e:
            print(f"Error en línea: {e}")
            if online_writer:
                online_writer.close()
                await online_writer.wait_closed()
                online_writer = None
        await asyncio.sleep(reconnect_delay)

async def TcPChaT(ip, port, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region, reconnect_delay=0.5):
    global whisper_writer, online_writer, auto_start_running, auto_start_task, stop_auto
    while True:
        try:
            reader, writer = await asyncio.open_connection(ip, int(port))
            whisper_writer = writer
            writer.write(bytes.fromhex(AutHToKen))
            await writer.drain()
            ready_event.set()

            if LoGinDaTaUncRypTinG.Clan_ID:
                clan_id = LoGinDaTaUncRypTinG.Clan_ID
                clan_compiled_data = LoGinDaTaUncRypTinG.Clan_Compiled_Data
                pK = await AuthClan(clan_id, clan_compiled_data, key, iv)
                if whisper_writer:
                    writer.write(pK)
                    await writer.drain()

            while True:
                data = await reader.read(9999)
                if not data:
                    break

                if data.hex().startswith("120000"):
                    try:
                        response = await DecodeWhisperMessage(data.hex()[10:])
                        uid = response.Data.uid
                        chat_id = response.Data.Chat_ID
                        inPuTMsG = response.Data.msg.strip().lower()
                        print(f"Mensaje: {inPuTMsG} de {uid}")

                        if inPuTMsG.startswith('/start '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                await safe_send_message(response.Data.chat_type, "[B][C][FF0000]Uso: /start <codigo_equipo>", uid, chat_id, key, iv)
                                continue
                            team_code = parts[1]
                            if not team_code.isdigit():
                                await safe_send_message(response.Data.chat_type, "[B][C][FF0000]El código de equipo debe ser numérico", uid, chat_id, key, iv)
                                continue
                            if auto_start_running:
                                await safe_send_message(response.Data.chat_type, "[B][C][FF0000]Auto inicio ya en ejecución. Usa /stop", uid, chat_id, key, iv)
                                continue
                            stop_auto = False
                            auto_start_running = True
                            await safe_send_message(response.Data.chat_type, f"[B][C][00FF00]iniciando bot en el equipo {team_code}\nUsa /stop para detener", uid, chat_id, key, iv)
                            auto_start_task = asyncio.create_task(auto_start_loop(team_code, uid, chat_id, response.Data.chat_type, key, iv, region))

                        elif inPuTMsG.strip() == '/stop':
                            if auto_start_running:
                                await stop_auto_loop()
                                await safe_send_message(response.Data.chat_type, "[B][C][00FF00]Auto inicio detenido", uid, chat_id, key, iv)
                            else:
                                await safe_send_message(response.Data.chat_type, "[B][C][FF0000]No hay auto inicio en ejecución", uid, chat_id, key, iv)

                        elif inPuTMsG.strip() in ('/help', 'help', '/menu', 'menu'):
                            help_parts = [
                                "[B][C][00FFFF]━━━ MENÚ SEBASXIT ━━━",
                                "[B][C][00FF00]╔═══ INICIAR ═══╗\n[B][C][FFFFFF]/start <codigo>\n[B][C][00FF00]╚══════════╝",
                                "[B][C][FF0000]╔═══ DETENER ═══╗\n[B][C][FFFFFF]/stop\n[B][C][FF0000]╚══════════╝",
                                "[B][C][00FFFF]╔═══ CREADOR ═══╗\n[B][C][FFFFFF]@sebasxit ✅️\n[B][C][00FFFF]╚══════════╝",
                            ]
                            
                            for part in help_parts:
                                await safe_send_message(response.Data.chat_type, part, uid, chat_id, key, iv)
                                await asyncio.sleep(0.5)

                    except Exception as e:
                        print(f"Error de decodificación: {e}")

            whisper_writer.close()
            await whisper_writer.wait_closed()
            whisper_writer = None
        except Exception as e:
            print(f"Error en chat: {e}")
            if whisper_writer:
                whisper_writer.close()
                await whisper_writer.wait_closed()
                whisper_writer = None
        await asyncio.sleep(reconnect_delay)

async def MaiiiinE():
    global CURRENT_BOT_UID, region
    
    if not os.path.exists("guest100067.dat"):
        print(f"{RED}❌ No se encontró el archivo guest100067.dat.{RESET}")
        return None
        
    with open("guest100067.dat", "r") as f:
        creds = json.load(f)
        
    try:
        uid = creds["guest_account_info"]["com.garena.msdk.guest_uid"]
        password = creds["guest_account_info"]["com.garena.msdk.guest_password"]
    except (KeyError, TypeError):
        print(f"{RED}❌ Formato de guest100067.dat inválido o faltan credenciales.{RESET}")
        return None

    print(f"{YELLOW}📱 Iniciando sesión con el UID: {uid}{RESET}")

    open_id, access_token = await GeNeRaTeAccEss(uid, password)
    if not open_id:
        print(f"{RED}❌ Error al obtener open_id/access_token{RESET}")
        return None

    payload = await EncRypTMajoRLoGin(open_id, access_token)
    login_resp = await MajorLogin(payload)
    if not login_resp:
        print(f"{RED}❌ MajorLogin falló{RESET}")
        return None
    auth = await DecRypTMajoRLoGin(login_resp)
    token = auth.token
    if not token:
        print(f"{RED}❌ Sin token{RESET}")
        return None

    token_data = {
        "token": token,
        "saved_at": time.time(),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "bot_uid": str(auth.account_uid),
        "region": getattr(auth, 'region', 'IND')
    }
    with open("token.json", "w") as f:
        json.dump(token_data, f, indent=2)

    url = auth.url
    region = getattr(auth, 'region', 'IND')
    bot_uid = auth.account_uid
    CURRENT_BOT_UID = str(bot_uid)
    key = auth.key
    iv = auth.iv
    timestamp = auth.timestamp

    login_data = await GetLoginData(url, payload, token)
    if not login_data:
        print(f"{RED}❌ GetLoginData falló{RESET}")
        return None
    ports = await DecRypTLoGinDaTa(login_data)
    online_ip, online_port = ports.Online_IP_Port.split(":")
    chat_ip, chat_port = ports.AccountIP_Port.split(":")

    auth_token = await xAuThSTarTuP(int(bot_uid), token, int(timestamp), key, iv)

    ready = asyncio.Event()
    task1 = asyncio.create_task(TcPChaT(chat_ip, chat_port, auth_token, key, iv, ports, ready, region))
    task2 = asyncio.create_task(TcPOnLine(online_ip, online_port, token, bot_uid, key, iv, auth_token))

    # =====================[ LUCK XIT SUCCESS BANNER ] =====================
    clear()
    print(f"{CYAN}")
    print(" ██╗     ██╗   ██╗ ██████╗██╗  ██╗    ██╗  ██╗██╗████████╗")
    print(" ██║     ██║   ██║██╔════╝██║ ██╔╝    ╚██╗██╔╝██║╚══██╔══╝")
    print(" ██║     ██║   ██║██║     █████╔╝      ╚███╔╝ ██║   ██║   ")
    print(" ██║     ██║   ██║██║     ██╔═██╗      ██╔██╗ ██║   ██║   ")
    print(" ███████╗╚██████╔╝╚██████╗██║  ██╗    ██╔╝ ██╗██║   ██║   ")
    print(" ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝   ╚═╝   ")
    print(f"{RESET}")
    print(f"{GREEN}╔════════════════════════════════════════════╗{RESET}")
    print(f"{GREEN}║ {WHITE}     ¡BOT EN LÍNEA CORRECTAMENTE!           {GREEN}║{RESET}")
    print(f"{GREEN}║ {YELLOW}     Ve al chat del juego y escribe: {CYAN}/help  {GREEN}║{RESET}")
    print(f"{GREEN}╚════════════════════════════════════════════╝{RESET}\n")
    # =======================================================================

    await asyncio.gather(task1, task2)

async def StarTinG():
    while True:
        try:
            await MaiiiinE()
        except Exception as e:
            print(f"{RED}Reiniciando debido a un error: {e}{RESET}")
            traceback.print_exc()
            await asyncio.sleep(5)

if __name__ == '__main__':
    # Comprobar permisos antes de iniciar el bot principal
    check_permission()
    asyncio.run(StarTinG())
