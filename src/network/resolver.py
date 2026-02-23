# Resolver para ver se a url tá pronta(a url da home do Shiro)
import aiodns
import asyncio

async def resolver_shiro_home():
    resolver = aiodns.DNSResolver()
    result = await resolver.query('', 'A')
    print(f"Shiro Home pronto no IP: {result[0].host}")

if __name__=="__main__":
    asyncio.run
