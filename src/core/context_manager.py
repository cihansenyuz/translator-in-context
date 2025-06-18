from typing import List

class ContextManager:
    def __init__(self):
        self.m_context_templates = {
            'european-partners': """This is a translation task of a service bulletin about television software.
- Do not use software terms heavily, be simple and clear for non-technical person.
- The translation should be formal and suitable for communication with European Balkan partners.
Examples: 1- 50” Charlie3/Beta2 kabinler AN şaside 052T50BE1 ve BE3 yerine 052T50HK1A kullanımı SW project_ID değişiklikleri aşağıdaki tabloya göre yapılmalıdır.
Tabloda TV’de BE1 ve BE3 Cell kullanıldığın da oluşan 56’lık kod, HK1 Cell kullanıldığında oluşan 56’lık kod mevcuttur. Project_ID panelin 56’lık koda göre belirlenmiştir.
Cell değişiminden sonra, PROJECT_ID'ler bölümünde belirtilen PID TV’ye set edilmelidir.
Translation:
For the 50” Charlie3/Beta2 cabinets with AN mainboard, instead of using 052T50BE1 and BE3, 052T50HK1A should be used. SW Project_ID changes should be made according to the table below.
The table shows the code begins with 056 when BE1 and BE3 cells are used on the TV, as well as the code begins with 056 when HK1 cell is used. The Project_ID is determined according to the code begins with 056 for the specific panel. After the Cell change, the PID specified in the PROJECT_ID section should be set to the TV.
2- XL Ürünlerde Kumanda Eşleşme Ekranında Kalma (eşleşme gerçekleşse bile ekranın geçiş yapmaması) problemi
Bu hatanın giderilebilmesi için TV yazılımının güncellenmesi gerekmektedir. Mevcut yazılım versiyonu güncel değilse, XL.V00.024.01-0028 veya daha yüksek bir versiyonla güncelleme yapılması önemlidir.

\\arcei34v\SOFTWARE\SERI\WEB\XL
bağlantısı üzerinden güncel yazılımlara erişim sağlayabilirsiniz

• Uygun yazılım, USB cihazının ana dizinine kopyalanır.
• USB, televizyonun USB girişine takılır.
• Televizyon, AC OFF/ON işlemi ile yeniden başlatılarak yazılım yükleme işlemi başlatılır.
• Yükleme işlemi tamamlandığında, hata giderilmiş olacaktır.
Translation:
Remains stuck in the Remote Control Pairing Screen (screen cannot be skipped even if pairing is succesfull) problem in XL mainboards.
In order to resolve this error, the TV software must be updated. If the current software version is outdated, it is important to update to XL.V00.024.01-0028 or higher.

You can access up-to-date software via the link
\\arcei34v\SOFTWARE\SERI\WEB\XL

• The appropriate software is copied to the main directory of the USB device.
• The USB is inserted into the USB port of the TV.
• The software installation process is started by restarting the TV with AC OFF/ON operation.
• Once the installation is complete, the error should be fixed.""",
            'chinese-partners': """This is a translation task of an email about television software project.
- Use software terms properly even if it is not used in the text, be clear for technical person.
- The translation should be culturally appropriate for Chinese partners.
- Do not add any additional explanations and comment."""
        }
        self.default_context = """- Two capital letters in the text indicates the mainboard project name."
- Alpha, Beta, Charlie, Delta and Echo are the cabinet names.
- In Turkish, the mainboard is also reffered as şasi or şase.
- In Turkish, USB refers to "USB bellek" or "USB flash bellek", not just "USB".
- "servisler" or "servis" may mean "technical service personal".
- "cell", "OC" refers to an opencell component of the panel of the television.
-"""

    def getContextPrompt(self, contexts: List[str]) -> str:
        """
        Generate a context prompt based on selected contexts
        
        Args:
            contexts: List of context identifiers
            
        Returns:
            str: Combined context prompt
        """
        prompts = [self.m_context_templates[ctx] for ctx in contexts if ctx in self.m_context_templates]
        return f"{self.default_context} {' '.join(prompts)}"
