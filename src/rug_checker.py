"""
⚠️ Rug Detector
Security analysis for token contracts
"""
import asyncio
import aiohttp
from typing import Dict, Optional
from dataclasses import dataclass

@dataclass
class SecurityReport:
    is_honeypot: bool
    is_mint_disabled: bool
    is_liquidity_locked: bool
    owner_can_mint: bool
    owner_is_treasury: bool
    go_plus_score: float
    honeypot_score: float

class RugChecker:
    def __init__(self, config: dict):
        self.honeypot_api = config.get('apis', {}).get('honeypot')
        self.goplus_api = config.get('apis', {}).get('goplus')
        
    async def check_rug(self, address: str, chain: str) -> SecurityReport:
        """Full security check"""
        results = SecurityReport(
            is_honeypot=False,
            is_mint_disabled=False,
            is_liquidity_locked=False,
            owner_can_mint=False,
            owner_is_treasury=False,
            go_plus_score=0.0,
            honeypot_score=0.0
        )
        
        # Check honeypot.is
        if self.honeypot_api:
            try:
                async with aiohttp.ClientSession() as sess:
                    async with sess.get(
                        f"https://api.honeypot.is/v2/standard/is-honeypot",
                        params={'address': address, 'chain': chain},
                        headers={'address': self.honeypot_api}
                    ) as resp:
                        if resp.status == 200:
                            data = await resp.json()
                            results.is_honeypot = not data.get('result', [True])[0]
                            results.honeypot_score = 1.0 if results.is_honeypot else 0.0
            except Exception as e:
                pass
                
        # Check GoPlus
        if self.goplus_api:
            try:
                async with aiohttp.ClientSession() as sess:
                    async with sess.get(
                        f"https://api.goplus.io/v2/token/security",
                        params={'chain': chain, 'contract': address},
                        headers={'x-api-key': self.goplus_api}
                    ) as resp:
                        if resp.status == 200:
                            data = await resp.json()
                            results.go_plus_score = data.get('data', {}).get('score', 0)
            except Exception as e:
                pass
                
        return results
        
    def is_safe(self, report: SecurityReport) -> bool:
        """Quick safety check"""
        return (
            not report.is_honeypot and
            report.go_plus_score > 70
        )