# http://github.com/hashicorp/memberlist

%global goipath         github.com/hashicorp/memberlist
%global commit          28424fb38c7c3e30f366b72b1a55f690d318d8f3


%gometa -i

Name:           %{goname}
Version:        0
Release:        0.14%{?dist}
Summary:        Golang package for gossip based membership and failure detection
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/armon/go-metrics)
BuildRequires: golang(github.com/hashicorp/go-msgpack/codec)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
# constant 2147483648 overflows int
%gochecks -d .

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md todo.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.git28424fb
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.20151121git28424fb
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git28424fb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git28424fb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git28424fb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git28424fb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git28424fb
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git28424fb
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git28424fb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.4.git28424fb
- Bump to upstream 28424fb38c7c3e30f366b72b1a55f690d318d8f3
  related: #1250471

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.gitdad1009
- Update to spec-2.1
  related: #1250471

* Wed Aug 05 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.1.gitdad1009
- Update spec file to spec-2.0
- Disable failing test - a golang bug
  resolves: #1250471

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitdad1009
- First package for Fedora
  resolves: #1212065

