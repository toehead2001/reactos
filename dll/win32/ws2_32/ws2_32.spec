500 stdcall WEP()
@ stdcall WPUCompleteOverlappedRequest(long ptr long long ptr)
@ stdcall WSAAccept(long ptr ptr ptr long)
@ stdcall WSAAddressToStringA(ptr long ptr ptr ptr)
@ stdcall WSAAddressToStringW(ptr long ptr ptr ptr)
102 stdcall WSAAsyncGetHostByAddr(long long ptr long long ptr long)
103 stdcall WSAAsyncGetHostByName(long long str ptr long)
105 stdcall WSAAsyncGetProtoByName(long long str ptr long)
104 stdcall WSAAsyncGetProtoByNumber(long long long ptr long)
107 stdcall WSAAsyncGetServByName(long long str str ptr long)
106 stdcall WSAAsyncGetServByPort(long long long str ptr long)
101 stdcall WSAAsyncSelect(long long long long)
108 stdcall WSACancelAsyncRequest(long)
113 stdcall WSACancelBlockingCall()
116 stdcall WSACleanup()
@ stdcall WSACloseEvent(long)
@ stdcall WSAConnect(long ptr long ptr ptr ptr ptr)
@ stdcall WSACreateEvent ()
@ stdcall WSADuplicateSocketA(long long ptr)
@ stdcall WSADuplicateSocketW(long long ptr)
@ stdcall WSAEnumNameSpaceProvidersA(ptr ptr)
@ stdcall WSAEnumNameSpaceProvidersW(ptr ptr)
@ stdcall WSAEnumNetworkEvents(long long ptr)
@ stdcall WSAEnumProtocolsA(ptr ptr ptr)
@ stdcall WSAEnumProtocolsW(ptr ptr ptr)
@ stdcall WSAEventSelect(long long long)
111 stdcall WSAGetLastError()
@ stdcall WSAGetOverlappedResult(long ptr ptr long ptr)
@ stdcall WSAGetQOSByName(long ptr ptr)
@ stdcall WSAGetServiceClassInfoA(ptr ptr ptr ptr)
@ stdcall WSAGetServiceClassInfoW(ptr ptr ptr ptr)
@ stdcall WSAGetServiceClassNameByClassIdA(ptr ptr ptr)
@ stdcall WSAGetServiceClassNameByClassIdW(ptr ptr ptr)
@ stdcall WSAHtonl(long long ptr)
@ stdcall WSAHtons(long long ptr)
@ stdcall WSAInstallServiceClassA(ptr)
@ stdcall WSAInstallServiceClassW(ptr)
@ stdcall WSAIoctl(long long ptr long ptr long ptr ptr ptr)
114 stdcall WSAIsBlocking()
@ stdcall WSAJoinLeaf(long ptr long ptr ptr ptr ptr long)
@ stdcall WSALookupServiceBeginA(ptr long ptr)
@ stdcall WSALookupServiceBeginW(ptr long ptr)
@ stdcall WSALookupServiceEnd(long)
@ stdcall WSALookupServiceNextA(long long ptr ptr)
@ stdcall WSALookupServiceNextW(long long ptr ptr)
@ stdcall WSANSPIoctl(long long ptr long ptr long ptr ptr)
@ stdcall WSANtohl(long long ptr)
@ stdcall WSANtohs(long long ptr)
@ stdcall WSAProviderConfigChange(ptr ptr ptr)
@ stdcall WSARecv(long ptr long ptr ptr ptr ptr)
@ stdcall WSARecvDisconnect(long ptr)
@ stdcall WSARecvFrom(long ptr long ptr ptr ptr ptr ptr ptr)
@ stdcall WSARemoveServiceClass(ptr)
@ stdcall WSAResetEvent(long)
@ stdcall WSASend(long ptr long ptr long ptr ptr)
@ stdcall WSASendDisconnect(long ptr)
@ stdcall WSASendTo(long ptr long ptr long ptr long ptr ptr)
109 stdcall WSASetBlockingHook(ptr)
@ stdcall WSASetEvent(long)
112 stdcall WSASetLastError(long)
@ stdcall WSASetServiceA(ptr long long)
@ stdcall WSASetServiceW(ptr long long)
@ stdcall WSASocketA(long long long ptr long long)
@ stdcall WSASocketW(long long long ptr long long)
115 stdcall WSAStartup(long ptr)
@ stdcall WSAStringToAddressA(str long ptr ptr ptr)
@ stdcall WSAStringToAddressW(wstr long ptr ptr ptr)
110 stdcall WSAUnhookBlockingHook()
@ stdcall WSAWaitForMultipleEvents(long ptr long long long)
@ stdcall WSApSetPostRoutine(ptr)
@ stdcall FreeAddrInfoW(ptr) freeaddrinfo
@ stdcall WSCDeinstallProvider(ptr ptr)
@ stdcall WSCEnableNSProvider(ptr long)
@ stdcall WSCEnumProtocols(ptr ptr ptr ptr)
@ stdcall WSCGetProviderPath(ptr ptr ptr ptr)
@ stdcall WSCInstallNameSpace(wstr wstr long long ptr)
@ stdcall WSCInstallProvider(ptr wstr ptr long ptr)
@ stdcall WSCUnInstallNameSpace(ptr)
@ stdcall WSCUpdateProvider(ptr ptr ptr long ptr)
@ stdcall WSCWriteNameSpaceOrder(ptr long)
@ stdcall WSCWriteProviderOrder(ptr long)
151 stdcall  __WSAFDIsSet(long ptr)
1   stdcall  accept(long ptr ptr)
2   stdcall  bind(long ptr long)
3   stdcall  closesocket(long)
4   stdcall  connect(long ptr long)
@ stdcall freeaddrinfo(ptr)
@ stdcall getaddrinfo(str str ptr ptr)
51  stdcall  gethostbyaddr(ptr long long)
52  stdcall  gethostbyname(str)
57  stdcall  gethostname(ptr long)
@ stdcall getnameinfo(ptr long ptr long ptr long long)
5   stdcall  getpeername(long ptr ptr)
53  stdcall  getprotobyname(str)
54  stdcall  getprotobynumber(long)
55  stdcall  getservbyname(str str)
56  stdcall  getservbyport(long str)
6   stdcall  getsockname(long ptr ptr)
7   stdcall  getsockopt(long long long ptr ptr)
8   stdcall  htonl(long)
9   stdcall  htons(long)
11  stdcall  inet_addr(str)
12  stdcall  inet_ntoa(ptr)
10  stdcall  ioctlsocket(long long ptr)
13  stdcall  listen(long long)
14  stdcall  ntohl(long)
15  stdcall  ntohs(long)
16  stdcall  recv(long ptr long long)
17  stdcall  recvfrom(long ptr long long ptr ptr)
18  stdcall  select(long ptr ptr ptr ptr)
19  stdcall  send(long ptr long long)
20  stdcall  sendto(long ptr long long ptr long)
21  stdcall  setsockopt(long long long ptr long)
22  stdcall  shutdown(long long)
23  stdcall  socket(long long long)
@ stdcall GetAddrInfoW(wstr wstr ptr ptr)
@ stdcall GetNameInfoW(ptr long wstr long wstr long long)