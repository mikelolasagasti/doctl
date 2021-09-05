

# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/digitalocean/doctl
%global goipath         github.com/digitalocean/doctl
Version:                1.64.0

%gometa

%global common_description %{expand:
The official command line interface for the DigitalOcean API}

%global golicenses      LICENSE.txt
%global godocs          CONTRIBUTING.md CHANGELOG.md README.md

Name:           doctl
Release:        1%{?dist}
Summary:        The official command line interface for the DigitalOcean API

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/blang/semver)
BuildRequires:  golang(github.com/digitalocean/godo)
BuildRequires:  golang(github.com/digitalocean/godo/util)
BuildRequires:  golang(github.com/docker/cli/cli/config)
BuildRequires:  golang(github.com/docker/cli/cli/config/types)
BuildRequires:  golang(github.com/dustin/go-humanize)
BuildRequires:  golang(github.com/fatih/color)
BuildRequires:  golang(github.com/gobwas/glob)
BuildRequires:  golang(github.com/golang/mock/gomock)
BuildRequires:  golang(github.com/gorilla/websocket)
BuildRequires:  golang(github.com/natefinch/pie)
BuildRequires:  golang(github.com/shiena/ansicolor)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/cobra/doc)
BuildRequires:  golang(github.com/spf13/viper)
BuildRequires:  golang(golang.org/x/crypto/ssh)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer/json)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/errors)
BuildRequires:  golang(k8s.io/client-go/pkg/apis/clientauthentication/v1beta1)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd/api)
BuildRequires:  golang(sigs.k8s.io/yaml)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(k8s.io/client-go/kubernetes/scheme)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build

%gobuild -o %{gobuilddir}/cmd/doctl %{goipath}/cmd/doctl

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/cmd/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE.txt
%doc CONTRIBUTING.md CHANGELOG.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Fri Sep 03 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.64.0-1
- Initial package

